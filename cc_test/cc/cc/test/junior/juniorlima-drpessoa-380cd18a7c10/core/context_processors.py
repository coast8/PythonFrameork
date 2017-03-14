# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from assessoria.models import Categoria, VideoPostagem, Postagem


from django.utils import timezone

def menusite(request):
    categorias = Categoria.objects.all()
    videos = VideoPostagem.objects.filter(postagem__publicar=True, postagem__categoria__id=5).order_by('-id')[:3]
    destaques_list = Postagem.objects.filter(publicar=True, destaque=True)[:5]
    return {'categorias':categorias,
            'videos': videos,
            'destaques_list': destaques_list,
            }