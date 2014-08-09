from django.forms import ModelForm
from foodd.models import *

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [ 'ingredient', 'name', 'uid', 'netamount',
                'tareamount', 'details' ]
