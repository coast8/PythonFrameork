# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Product, Category

# Class-Based Views
# ccbv.co.uk

class ProductListView(generic.ListView):

    model = Product #ja faz o Objects.All()
    template_name = 'catalog/product_list.html'
    context_object_name = 'products' #contexto
    paginate_by = 3


product_list = ProductListView.as_view()


class CategoryListView(generic.ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'product_list'
    paginate_by = 3

    #lista os produtos de uma categoria
    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    # adicionando variaveis no contexto
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


category = CategoryListView.as_view()


def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)
