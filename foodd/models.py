from django.db import models
from django.db.models import Q

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
    uid        = models.IntegerField(primary_key=True)
    ingredient = models.ForeignKey(AbstractIngredient)
    name       = models.CharField(max_length=255)
    netamount  = models.FloatField()
    tareamount = models.FloatField(blank=True, default=0)
    details    = models.TextField(blank=True)

    def __str__(self): return self.name

class Stock(models.Model):
    product   = models.ForeignKey(Product)
    remaining = models.FloatField()
    expiry    = models.DateField(blank=True,null=True)

    def __str__(self): return "%s of %s" % (self.remaining,
            self.product)

class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(AbstractIngredient)
    properties = models.ManyToManyField(Property, null=True, blank=True)
    optional   = models.BooleanField(default=False)
    amount     = models.FloatField()

    def find_stocks(self):
        return Stock.objects.filter(Q(product__ingredient=self.ingredient) |
                                    Q(product__ingredient__provides=self.ingredient) |
                                    Q(product__ingredient__properties__in=self.properties.all()) |
                                    Q(product__ingredient__properties__in=self.ingredient.properties.all()))

    def __str__(self): return "%s of %s" % (self.amount,
            self.ingredient)

class Recipe(models.Model):
    name            = models.CharField(max_length=255)
    ingredients     = models.ManyToManyField(RecipeIngredient)
    instructions    = models.TextField(blank=True,null=True)

    def __str__(self): return self.name

    def has_stocks(self):
        return all((ingredient.find_stocks() for ingredient in
            self.ingredients.all()))
