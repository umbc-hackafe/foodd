from django.core import serializers
from django.http import HttpResponse
from foodd.models import Recipe

def list_recipes(request):
    return HttpResponse(serializers.serialize("json",
        Recipe.objects.all()), mimetype="application/json")
