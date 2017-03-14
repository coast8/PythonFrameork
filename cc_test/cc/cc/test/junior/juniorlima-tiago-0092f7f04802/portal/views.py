# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.shortcuts import get_object_or_404, render

from portal.models import Postagem

def home(request):
    destaques = Postagem.objects.filter(publicar=True).order_by('-id')[0:3]
    noticias = Postagem.objects.filter(publicar=True).order_by('-id')[3:9]
    return render(request, 'portal/index.html', {
        'destaques': destaques,
        'noticias': noticias,
    })

def noticia(request, slugcategoria, slug):
    noticia = get_object_or_404(Postagem, categoria__slug=slugcategoria, slug=slug)
    return render(request, 'portal/postagem.html', {
        'noticia': noticia,
    })