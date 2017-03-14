from django.shortcuts import render

from .models import Product
from .models import Category
# Create your views here.


def lista_categorias(request):
	return render(request, 'catalago/lista_categorias.html')

def lista_produtos(request):
	context = {
		'lista_produtos': Product.objects.all()
	}
	return render(request, 'catalago/lista_produtos.html', context)

def categoria(request, slug):
	category = Category.objects.get(slug=slug)
	context = {
		'current_category': category,
        'product_list': Product.objects.filter(category=category),
	}
	return render(request, 'catalago/categoria.html', context)


def produto(request, slug):
	product = Product.objects.get(slug=slug)
	context = {
		'product': product
	}
	return render(request, 'catalago/produto.html', context)