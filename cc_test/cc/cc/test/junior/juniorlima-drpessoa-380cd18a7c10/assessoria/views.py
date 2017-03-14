# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from datetime import datetime

from django.shortcuts import render, get_object_or_404

from assessoria.models import Postagem, VideoPostagem, Evento
from galeria.models import Galeria, Image
def index(request):
    destaques_lista = Postagem.objects.filter(publicar=True).order_by('-id')[0:3]
    noticias_list = Postagem.objects.filter(publicar=True).order_by('-id')[3:9]
    return render(request, 'site/nova-index.html',{
        'noticias_list': noticias_list,
        'destaques_lista': destaques_lista,
    })

def agenda(request):
    agenda_list = Evento.objects.filter(postagem__publicar=True, postagem__categoria__nome='Agenda', data_evento__gte=datetime.now()).order_by('-id')
    return render(request, 'site/agenda.html',{
        'agenda_list': agenda_list,
    })

def contato(request):
    return render(request, 'site/contato.html',{

    })

def galeria(request, slug):
    galeria_object = get_object_or_404(Galeria, slug=slug)
    fotos = Image.objects.filter(galeria=galeria_object)
    return render(request, 'site/galeria.html',{
        'galeria_object': galeria_object,
        'fotos': fotos,
    })

def galerias(request):
    galeria_list = Galeria.objects.filter(publicar=True)
    return render(request, 'site/galerias.html',{
        'galeria_list': galeria_list
    })

def namidia(request):
    na_midia_list = VideoPostagem.objects.filter(postagem__publicar=True).order_by('-id')
    return render(request, 'site/namidia.html',{
        'na_midia_list': na_midia_list,
    })

def noticia(request, slug):
    noticia = get_object_or_404(Postagem, slug=slug)
    destaques_list = Postagem.objects.filter(publicar=True).order_by('-id')[:3]
    video_last = VideoPostagem.objects.filter(postagem__publicar=True)[:1]
    return render(request, 'site/noticia.html',{
        'noticia': noticia,
        'destaques_list': destaques_list,
        'video_last': video_last,
    })


def noticias(request):
    noticias_list = Postagem.objects.filter(publicar=True).order_by('-id')
    return render(request, 'site/noticias.html',{
        'noticias_list': noticias_list,
    })

def perfil(request):
    return render(request, 'site/perfil.html',{

    })

def timeline(request):
    timeline_list = Evento.objects.filter(postagem__publicar=True, postagem__categoria__nome='Agenda', data_evento__lte=datetime.now()).order_by('-data_evento')
    return render(request, 'site/timeline.html',{
        'timeline_list': timeline_list,
    })

def voluntariado(request):
    return render(request, 'site/voluntario.html',{

    })

def amigos(request):
    return render(request, 'site/amigo.html',{

    })
