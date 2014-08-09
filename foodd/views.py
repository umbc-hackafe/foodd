from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from foodd.models import *
from foodd.forms import *

def edit(request, kind, key=None):
    kind_class = None
    form = None
    if kind == "property":
        kind_class = Property
        form = PropertyForm
    elif kind == "ingredient":
        kind_class = AbstractIngredient
        form = AbstractIngredientForm
    elif kind == "product":
        kind_class = Product
        form = ProductForm
    elif kind == "stock":
        kind_class = Stock
        form = StockForm
    elif kind == "recipeingredient":
        kind_class = RecipeIngredient
        form = RecipeIngredientForm
    elif kind == "recipe":
        kind_class = Recipe
        form = RecipeForm
    else:
        return HttpResponse("Page Not Found", status=404)

    if key:
        item = kind_class.objects.get(pk=key)
    else:
        item = kind_class()

    if request.method == "POST":
        form = form(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return HttpResponse('Saved successfully', status=201)
        return HttpResponse('Form invalid', status=400)
    return render(request, "edit_product.html", {
        "kind":    kind,
        "product": item,
        "form":    form(None, instance=item)
        })
