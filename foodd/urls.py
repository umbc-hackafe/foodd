from django.conf.urls import patterns, include, url

from foodd import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foodd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^add/(?P<kind>[a-z]+)/?', views.edit, name="Add"),
    url(r'^edit/(?P<kind>[a-z]+)/(?P<key>[0-9]+)/?', views.edit, name="Edit"),
    url(r'^view/recipes/?', views.list_recipes, name="List Recipes"),
    url(r'^view/recipe/(?P<recipe_id>[0-9]+)', views.view_recipe, name="View Recipe")
)
