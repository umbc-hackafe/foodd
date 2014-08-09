from django.contrib import admin
import foodd.models

admin.site.register(foodd.models.Property)
admin.site.register(foodd.models.AbstractIngredient)
admin.site.register(foodd.models.Package)
admin.site.register(foodd.models.Stock)
admin.site.register(foodd.models.Recipe)
admin.site.register(foodd.models.RecipeIngredient)
