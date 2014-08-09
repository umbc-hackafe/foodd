from django.utils import simplejson
from django.http import HttpResponse
from foodd.models import Recipe

def list_recipes(request):
    recipes = Recipe.objects.all()
    return HttpResponse(simplejson.dumps(list(recipes)), mimetype="application/json")
