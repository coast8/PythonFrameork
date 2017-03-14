from django.conf.urls import url

from catalog.views import product_list
from catalog.views import product

urlpatterns = [

	url(r'^lista-de-produtos/$', product_list, name='product_list'),
	url(r'^produto/(?P<slug>[\w_-]+)/$', product, name='product'),
	
]