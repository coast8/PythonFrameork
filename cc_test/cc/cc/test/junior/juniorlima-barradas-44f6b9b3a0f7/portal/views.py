# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.shortcuts import render, get_object_or_404

from ads.models import PubliImagem
from portal.models import Postagem, Categoria
from blogs.models import Blog, NoticiaBlog

def home(request):
    ultimas = Postagem.objects.filter(publicar=True, destaque=False).exclude(categoria__id=7).order_by('-id')[:11]
    destaques = Postagem.objects.filter(publicar=True, destaque=True).exclude(categoria__id=7).order_by('-id')[:4]
    tv = Postagem.objects.filter(publicar=True, destaque=False, categoria__id=7).order_by('-id')[:3]
    noticias_blog_on = NoticiaBlog.objects.filter(publicar=True, destaque=True).order_by('-id')[:1]
    noticias_blog_off = NoticiaBlog.objects.filter(publicar=True, destaque=False).order_by('-id')[:6]

    return render(request, 'site/index.html', {
        'ultimas': ultimas,
        'destaques': destaques,
        'tv': tv,
        'noticias_blog_on': noticias_blog_on,
        'noticias_blog_off': noticias_blog_off,
    })

def noticias(request):
    noticias = Postagem.objects.filter(publicar=True).order_by('-id')[:21]
    return render(request, 'site/noticias.html', {
        'noticias': noticias,
    })

def noticia(request, slug):
    noticia = get_object_or_404(Postagem, slug=slug)
    relacionadas = Postagem.objects.filter(categoria__id=noticia.categoria_id).exclude(pk=noticia.pk).order_by('-id')[:4]
    return render(request, 'site/noticia.html', {
        'noticia': noticia,
        'relacionadas': relacionadas,
    })

def categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    noticias_list = Postagem.objects.filter(categoria__id=categoria.id).order_by('-id')
    return render(request, 'site/categoria.html', {
        'categoria': categoria,
        'noticias_list': noticias_list,
    })

def blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    noticias_blog = NoticiaBlog.objects.filter(publicar=True, blog__blog__id=blog.id)
    return render(request, 'site/blog.html', {
        'blog': blog,
        'noticias_blog': noticias_blog,
    })

def noticia_blog(request, blog, slug):
    noticia = get_object_or_404(NoticiaBlog, blog__blog__slug=blog, slug=slug)
    relacionadas = NoticiaBlog.objects.filter(blog__blog__id=noticia.blog.blog.id).exclude(pk=noticia.pk).order_by('-id')[:4]
    return render(request, 'site/noticia-blog.html', {
        'noticia': noticia,
        'relacionadas': relacionadas,
    })