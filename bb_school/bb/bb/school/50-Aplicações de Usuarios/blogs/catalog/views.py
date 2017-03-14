from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import Category, Product

class ProductListView(generic.ListView):

	model = Product
	template_name = 'catalog/product_list.html'
	context_object_name = 'products'

product_list = ProductListView.as_view()


def product(request, slug):
	product = Product.objects.get(slug=slug)

	context = {
		'product': product
	}
	return render(request, 'catalog/product.html', context)


