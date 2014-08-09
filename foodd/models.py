from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=255)

DIMENSIONS = (
        (0, "Discrete"),
        (1, "Volume"),
        (2, "Mass")
)

class Dimensionality(models.Model):
    dimension = models.IntegerField(choices=DIMENSIONS)

class AbstractIngredient(models.Model):
    name           = models.CharField(max_length=255)
    provides       = models.ManyToManyField("self")
    properties     = models.ManyToManyField(Property)
    dimensionality = models.ForeignKey(Dimensionality)
    details        = models.TextField()
