from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self): return self.name

DIMENSIONS = (
        (0, "Discrete"),
        (1, "Volume"),
        (2, "Mass")
)

class AbstractIngredient(models.Model):
    name           = models.CharField(max_length=255)
    provides       = models.ManyToManyField("self", null=True, blank=True)
    properties     = models.ManyToManyField(Property, blank=True)
    dimensionality = models.IntegerField(choices=DIMENSIONS)
    details        = models.TextField(blank=True)

    def __str__(self): return self.name

class Product(models.Model):
    ingredient = models.ForeignKey(AbstractIngredient)
    name       = models.CharField(max_length=255)
    uid        = models.IntegerField()
    netamount  = models.FloatField()
    tareamount = models.FloatField(blank=True, default=0)
    details    = models.TextField(blank=True)

    def __str__(self): return self.name

class Stock(models.Model):
    product   = models.ForeignKey(Product)
    remaining = models.FloatField()
    expiry    = models.DateField(null=True)

    def __str__(self): return "%s of %s" % (self.remaining,
            self.product)

class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(AbstractIngredient)
    properties = models.ManyToManyField(Property, null=True, blank=True)
    optional   = models.BooleanField(default=False)
    amount     = models.FloatField()

    def __str__(self): return "%s of %s" % (self.amount,
            self.ingredient)

class Recipe(models.Model):
    name            = models.CharField(max_length=255)
    ingredients     = models.ManyToManyField(RecipeIngredient)
    instructions    = models.TextField(null=True)

    def __str__(self): return self.name
