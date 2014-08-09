from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from foodd.models import *
from foodd.forms import *

def list_recipes(request):
    return HttpResponse(serializers.serialize("json",
        Recipe.objects.all()), mimetype="application/json")

def add_product(request, uid):
    if request.method == "POST":
        # Select an instance of the product based on the uid in the URL.
        try:
            product = Product.objects.get(uid=uid)
        except Product.DoesNotExist:
            product = Product(uid=uid)

        # Parse the form as it applies to the product.
        form = ProductForm(request.POST, instance=product)

        # If the form is valid, update the database with it.
        if form.is_valid():
            form.save()
            return HttpResponse('Saved successfully', status=201)

        return HttpResponse('Form invalid', status=400)

    try:
        product = Product.objects.get(uid=uid)
    except Product.DoesNotExist:
        product = Product(uid=uid)

    return render(request, "edit_product.html", {
        "product": product,
        "form":    ProductForm(None, instance=product)
        })
