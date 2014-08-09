from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from foodd.models import *
from foodd.forms import *

def list_recipes(request):
    return HttpResponse(serializers.serialize("json",
        Recipe.objects.all()), mimetype="application/json")

def add_product(request, uid=None):
    print("UID is", uid)
    product = None
    if uid:
        try:
            product = Product.objects.get(uid=uid)
        except Product.DoesNotExist:
            product = Product(uid=uid)

    if request.method == "POST":
        # Parse the form as it applies to the product.
        form = ProductForm(request.POST, instance=product)

        # If the form is valid, update the database with it.
        if form.is_valid():
            form.save()
            return HttpResponse('Saved successfully', status=201)

        return HttpResponse('Form invalid', status=400)

    return render(request, "edit_product.html", {
        "product": product,
        "form":    ProductForm(None, instance=product)
        })
