from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=255)

DIMENSIONS = (
        (0, "Discrete"),
        (1, "Volume"),
        (2, "Mass")
)

class AbstractIngredient(models.Model):
    name           = models.CharField(max_length=255)
    provides       = models.ManyToManyField("self", null=True)
    properties     = models.ManyToManyField(Property)
    dimensionality = models.IntegerField(choices=DIMENSIONS)
    details        = models.TextField(null=True)

class Package(models.Model):
    ingredient = models.ForeignKey(AbstractIngredient)
    name       = models.CharField(max_length=255)
    uid        = models.IntegerField()
    netamount  = models.FloatField()
    tareamount = models.FloatField()
    details    = models.TextField(null=True)

class Stock(models.Model):
    package   = models.ForeignKey(Package)
    remaining = models.FloatField()
    expiry    = models.DateField(null=True)

class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(AbstractIngredient)
    properties = models.ManyToManyField(Property, null=True)
    optional   = models.BooleanField(default=False)
    amount     = models.FloatField()

class Recipe(models.Model):
    ingredients     = models.ManyToManyField(RecipeIngredient)
    instructions    = models.TextField(null=True)
