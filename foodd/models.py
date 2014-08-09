from django.db import models

class AbstractIngredient(models.Model):
    name           = models.CharField()
    provides       = models.ManyToMany(AbstractIngredient)
    properties     = models.ManyToMany(Property)
    dimensionality = models.ForeignKey(Dimensionality)
    details        = models.TextField()

class Property(models.Model):
    name = models.CharField()

class Dimensionality(models.Model):
    dimension = models.CharField()
