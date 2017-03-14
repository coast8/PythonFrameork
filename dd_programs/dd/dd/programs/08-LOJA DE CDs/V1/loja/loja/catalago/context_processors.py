# coding=utf-8

from .models import Category


#funçao usado para listar as categorias.
def categories(request):
    return {
        'categories': Category.objects.all()
    }
