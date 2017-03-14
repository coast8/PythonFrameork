from django.shortcuts import render

from catalogo.models import Marca, Produto

def home(request):
    marca_list = Marca.objects.filter()
    return render(request, 'melo/index.html', {
    })

def marca(request, slugcategoria):
    return render(request, 'melo/marca.html', {
    })

def produto(request, slugcategoria, slug):
    return render(request, 'melo/produto.html', {
    })
