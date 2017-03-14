# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from portal.models import Categoria, Postagem
from ads.models import PubliImagem
from blogs.models import Blog
from blogs.models import NoticiaBlog
from django.utils import timezone

def menusite(request):
    categorias = Categoria.objects.all()
    blogs = Blog.objects.filter(ativo=True)
    #videos = VideoPostagem.objects.filter(postagem__publicar=True, postagem__categoria__id=5).order_by('-id')[:3]
    ads_cab_01 = PubliImagem.objects.filter(dataentrada__lte=timezone.now(), datasaida__gte=timezone.now(), posicao__id=1, ativo=True).order_by('-id')[:1]
    ads_cab_02 = PubliImagem.objects.filter(dataentrada__lte=timezone.now(), datasaida__gte=timezone.now(), posicao__id=2, ativo=True).order_by('-id')[:1]
    ads_cab_03 = PubliImagem.objects.filter(dataentrada__lte=timezone.now(), datasaida__gte=timezone.now(), posicao__id=3, ativo=True).order_by('-id')[:1]
    ads_ret_01 = PubliImagem.objects.filter(dataentrada__lte=timezone.now(), datasaida__gte=timezone.now(), posicao__id=4, ativo=True).order_by('-id')[:1]
    ads_ret_02 = PubliImagem.objects.filter(dataentrada__lte=timezone.now(), datasaida__gte=timezone.now(), posicao__id=5, ativo=True).order_by('-id')[:1]
    ads_bot_all = PubliImagem.objects.filter(dataentrada__lte=timezone.now(), datasaida__gte=timezone.now(), posicao__id=6, ativo=True).order_by('-id')[:4]
    revista = Postagem.objects.filter(categoria__id=8)[:1]
    ultima_lista = NoticiaBlog.objects.filter(publicar=True).order_by('-id')[:5]
    print ads_cab_01
    return {'categorias':categorias,
            'blogs': blogs,
            'ads_cab_01': ads_cab_01,
            'ads_cab_02': ads_cab_02,
            'ads_cab_03': ads_cab_03,
            'ads_ret_01': ads_ret_01,
            'ads_ret_02': ads_ret_02,
            'ads_bot_all': ads_bot_all,
            'revista': revista,
            'ultima_lista': ultima_lista,
            }