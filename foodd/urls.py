from django.conf.urls import patterns, include, url

from foodd import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foodd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^recipes/', views.list_recipes, name="List Recipes"),
    url(r'^products/edit/(?P<uid>[0-9]+)/?', views.add_product, \
        name="Edit Product"),
    url(r'^products/edit/', views.add_product, \
        name="Add Product")
)
