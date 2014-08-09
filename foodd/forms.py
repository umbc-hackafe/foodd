from django.forms import ModelForm
from foodd.models import *

class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = [ 'name' ]

class IngredientForm(ModelForm):
    class Meta:
        model = AbstractIngredient
        fields = [ 'name', 'provides', 'properties', 'dimensionality', 'details' ]

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [ 'ingredient', 'name', 'uid', 'netamount',
                'tareamount', 'details' ]

class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = [ 'product', 'remaining', 'expiry' ]

class RecipeIngredientForm(ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = [ 'ingredient', 'properties', 'optional', 'amount' ]

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = [ 'name', 'ingredients', 'instructions' ]
