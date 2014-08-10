from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from foodd.models import *
from foodd.forms import *

urlmap = {
        "property": (Property, PropertyForm),
        "ingredient": (AbstractIngredient, IngredientForm),
        "product": (Product, ProductForm),
        "stock": (Stock, StockForm),
        "recipeingredient": (RecipeIngredient, RecipeIngredientForm),
        "recipe": (Recipe, RecipeForm)
        }


def edit(request, kind, key=None):
    if kind in urlmap:
        kind_class, form = urlmap[kind]
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

def view_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, "view_recipe.html", {
        "recipe": recipe
    })
