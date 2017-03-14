# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext, Context
from igenius.forms import *
from models import *
from publicidades.models import *
from blogs.models import *
from times.models import *
from django import forms
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from noticias.models import *


def homepage(request):
    manchete = Noticia.objects.filter(manchete__icontains=1, extra__icontains=0, publicar__icontains=1).order_by(
        '-datapublicacao')[:2]
    extra = Noticia.objects.filter(manchete__icontains=0, extra__icontains=1, publicar__icontains=1).order_by(
        '-datapublicacao')[:1]
    noticias = Noticia.objects.filter(manchete__icontains=0, publicar__icontains=1, extra__icontains=0,
                                      subcategoria__categoria__slugcategoria__contains='noticias').order_by(
        '-datapublicacao')
    plantao = Noticia.objects.filter(publicar__icontains=1).order_by('-datapublicacao')
    blogs = BlogUsuario.objects.filter(blog__ativo__icontains=1).order_by('-blog')
    blogueiras = BlogUsuario.objects.filter(blog__ativo__icontains=1).order_by('?')
    team = Times.objects.all().order_by('-nome')
    entretenimento = Noticia.objects.filter(manchete__icontains=0, publicar__icontains=1, extra__icontains=0,
                                            subcategoria__categoria__slugcategoria__contains='entretenimento').order_by(
        '-datapublicacao')
    politica = Noticia.objects.filter(manchete__icontains=0, publicar__icontains=1, extra__icontains=0,
                                      subcategoria__categoria__slugcategoria__contains='politica').order_by(
        '-datapublicacao')
    videos = Noticia.objects.filter(manchete__icontains=0, publicar__icontains=1, extra__icontains=0,
                                    subcategoria__categoria__slugcategoria__contains='videos').order_by(
        '-datapublicacao')
    esportes = Noticia.objects.filter(manchete__icontains=0, publicar__icontains=1, extra__icontains=0,
                                      subcategoria__categoria__slugcategoria__contains='esportes').order_by(
        '-datapublicacao')

    publicidade = Publicidade.objects.filter(data_entrada__lte=datetime.now(), data_saida__gte=datetime.now())

    categoria = SubCategoria.objects.all().order_by('?')[:4]
    categorias = CategoriaNoticia.objects.all().order_by('nome')
    subcategorias = SubCategoria.objects.all().order_by('nome')

    categoriaNoticias = SubCategoria.objects.filter(categoria__slugcategoria__contains='noticias').order_by('-nome')
    bairros = Bairros.objects.all().order_by('-nome')

    return render_to_response('igenius/index.html', locals(), context_instance=RequestContext(request))
    # return render_to_response('igenius/index-o.html', locals(), context_instance=RequestContext(request))


def contato(request):
    noticias = Noticia.objects.filter(publicar__icontains=1).order_by('-datapublicacao')
    categoria = SubCategoria.objects.all().order_by('?')[:4]

    return render_to_response('igenius/contato.html', locals(), context_instance=RequestContext(request))
    # return render_to_response('igenius/index-o.html', locals(), context_instance=RequestContext(request))


def sobre(request):
    noticias = Noticia.objects.filter(publicar__icontains=1).order_by('-datapublicacao')
    categoria = SubCategoria.objects.all().order_by('?')[:4]

    return render_to_response('igenius/sobre.html', locals(), context_instance=RequestContext(request))
    # return render_to_response('igenius/index-o.html', locals(), context_instance=RequestContext(request))


def noticiainterna(request, slugcategoria, slugsubcategoria, slugnoticia):
    blogs = BlogUsuario.objects.filter(blog__ativo__icontains=1).order_by('-blog')
    plantao = Noticia.objects.filter(publicar__icontains=1).order_by('-datapublicacao')
    lidas = Noticia.objects.filter(publicar__icontains=1, subcategoria__categoria__slugcategoria=slugcategoria,
                                   subcategoria__slugsubcategoria=slugsubcategoria).order_by('-hits')[:7]
    team = Times.objects.all().order_by('-nome')

    noticia = get_object_or_404(Noticia, subcategoria__categoria__slugcategoria=slugcategoria,
                                subcategoria__slugsubcategoria=slugsubcategoria, slugnoticia=slugnoticia)
    noticias = Noticia.objects.filter(manchete__icontains=0, publicar__icontains=1).order_by('-datapublicacao')
    subcategoria = SubCategoria.objects.filter(categoria__slugcategoria=slugcategoria)
    publicidade = Publicidade.objects.filter(data_entrada__lte=datetime.now(), data_saida__gte=datetime.now())

    relacionada = Noticia.objects.filter(manchete__icontains=0, publicar__icontains=1,
                                         subcategoria__categoria__slugcategoria__contains=slugcategoria,
                                         subcategoria__slugsubcategoria=slugsubcategoria).order_by(
        '-datapublicacao')
    noti = Noticia.objects.all().order_by('datapublicacao')[:6]

    # artigofooter = Noticia.objects.filter(nomecategoria__id = 5,publicar__icontains=1,manchete__icontains=0).order_by('-datapublicacao')[:3]
    # blogfooter = NoticiaBlog.objects.all().order_by('-datapublicacao').filter(publicar__icontains=1)[:3]
    #ilhainternaquadrada = Publicidade.objects.filter(ativo__exact='1',tipo__exact='7',dataentrada__lte=datetime.now(),datasaida__gte=datetime.now())[:1]
    #ilhainternawide = Publicidade.objects.filter(ativo__exact='1',tipo__exact='8',dataentrada__lte=datetime.now(),datasaida__gte=datetime.now())[:1]
    #objeto = TagItem.objects.filter(object_id=noticias.id)

    categorias = CategoriaNoticia.objects.all().order_by('nome')
    subcategorias = SubCategoria.objects.all().order_by('nome')

    if noticiainterna:
        if not request.session.get('noticia_hits_%s' % slugnoticia):
            noticia.hits = noticia.hits + 1
            noticia.save()
            request.session['noticia_hits_%s' % slugnoticia] = True

    return render_to_response('igenius/noticia-interna.html', locals(), context_instance=RequestContext(request))


def noticiablog(request, slugblog, slug):
    dblog = get_object_or_404(BlogUsuario, blog__slugblog=slugblog)

    lidas = Noticia.objects.filter(publicar__icontains=1).order_by('-hits')[:7]
    blogs = BlogUsuario.objects.filter(blog__ativo__icontains=1).order_by('-blog')
    noticia = get_object_or_404(NoticiaBlog, blog__blog__slugblog=slugblog, slug=slug)
    noticias = Noticia.objects.filter(manchete__icontains=0, publicar__icontains=1).order_by('-datapublicacao')
    plantao = Noticia.objects.filter(publicar__icontains=1).order_by('-datapublicacao')

    blog = get_object_or_404(Blog, slugblog=slugblog)

    publicidade = Publicidade.objects.filter(data_entrada__lte=datetime.now(), data_saida__gte=datetime.now())

    relacionada = NoticiaBlog.objects.filter(publicar__icontains=1, blog__blog__slugblog=slugblog).order_by(
        '-criado_em')
    noti = Noticia.objects.all().order_by('-datapublicacao')[:6]

    categorias = CategoriaNoticia.objects.all().order_by('nome')
    subcategorias = SubCategoria.objects.all().order_by('nome')

    return render_to_response('igenius/noticia-interna-blog.html', locals(), context_instance=RequestContext(request))


def patrocinado(request, slugpublicidade):
    publicidade = get_object_or_404(Publicidade, slugpublicidade=slugpublicidade)

    categorias = CategoriaNoticia.objects.all().order_by('nome')
    subcategorias = SubCategoria.objects.all().order_by('nome')

    return render_to_response('igenius/patrocinado-interna.html', locals(), context_instance=RequestContext(request))


def categoria(request, slugcategoria):
    blogs = BlogUsuario.objects.filter(blog__ativo__icontains=1).order_by('-blog')
    publicidade = Publicidade.objects.filter(data_entrada__lte=datetime.now(), data_saida__gte=datetime.now())
    lidas = Noticia.objects.filter(publicar__icontains=1,
                                   subcategoria__categoria__slugcategoria__contains=slugcategoria).order_by('-hits')[:7]
    plantao = Noticia.objects.filter(publicar__icontains=1).order_by('-datapublicacao')[:5]
    team = Times.objects.all().order_by('-nome')

    noticiasmanchete = Noticia.objects.filter(manchete__icontains=1, publicar__icontains=1,
                                              subcategoria__categoria__slugcategoria__contains=slugcategoria).order_by(
        '-datapublicacao')[:30]
    noticias = Noticia.objects.filter(manchete__icontains=0, publicar__icontains=1,
                                      subcategoria__categoria__slugcategoria__contains=slugcategoria).order_by(
        '-datapublicacao')[:30]

    cat = get_object_or_404(CategoriaNoticia, slugcategoria__contains=slugcategoria)
    subcategoria = SubCategoria.objects.filter(categoria__slugcategoria__contains=slugcategoria).order_by('-nome')

    categorias = CategoriaNoticia.objects.all().order_by('nome')
    subcategorias = SubCategoria.objects.all().order_by('nome')

    return render_to_response('igenius/categoria-home.html', locals(), context_instance=RequestContext(request))


def bairro(request, sluguf, slugcidade, slugbairro):
    # blogs = BlogUsuario.objects.filter(blog__ativo__icontains = 1).order_by('-blog')
    # publicidade = Publicidade.objects.filter(data_entrada__lte=datetime.now(), data_saida__gte=datetime.now())
    #lidas = Noticia.objects.filter(publicar__icontains=1,subcategoria__categoria__slugcategoria__contains=slugcategoria).order_by('-hits')[:7]
    #plantao = Noticia.objects.filter(publicar__icontains=1).order_by('-datapublicacao')[:5]
    #team = Times.objects.all().order_by('-nome')

    #noticiasmanchete = Noticia.objects.filter(manchete__icontains=1, publicar__icontains=1,
    #                                         subcategoria__categoria__slugcategoria__contains=slugcategoria).order_by(
    #    '-datapublicacao')[:30]
    noticias = NoticiaLocal.objects.filter(manchete__icontains=0, publicar__icontains=1,
                                           bairro__cidade__uf__sluguf=sluguf, bairro__cidade__slugcidade=slugcidade,
                                           bairro__slugbairro=slugbairro).order_by(
        '-datapublicacao')[:30]

    cat = get_object_or_404(Bairros, slugbairro__contains=slugbairro)
    #subcategoria = SubCategoria.objects.filter(categoria__slugcategoria__contains=slugcategoria).order_by('-nome')

    categorias = Bairros.objects.all().order_by('nome')
    subcategorias = Bairros.objects.all().order_by('nome')

    return render_to_response('igenius/categoria-home-bairro.html', locals(), context_instance=RequestContext(request))


def blogs(request):
    plantao = Noticia.objects.filter(publicar__icontains=1).order_by('-datapublicacao')

    lidas = Noticia.objects.filter(publicar__icontains=1).order_by('-hits')[:7]
    publicidade = Publicidade.objects.filter(data_entrada__lte=datetime.now(), data_saida__gte=datetime.now())
    noticias = NoticiaBlog.objects.filter(blog__blog__ativo__icontains=1).order_by('-criado_em')
    blogs = BlogUsuario.objects.filter(blog__ativo__icontains=1).order_by('-blog')

    categorias = CategoriaNoticia.objects.all().order_by('nome')
    subcategorias = SubCategoria.objects.all().order_by('nome')

    return render_to_response('igenius/blogs.html', locals(), context_instance=RequestContext(request))


def timeInterna(request, slugtime):
    lidas = Noticia.objects.filter(publicar__icontains=1).order_by('-hits')[:7]

    blogs = BlogUsuario.objects.all().order_by('-blog')
    publicidade = Publicidade.objects.filter(data_entrada__lte=datetime.now(), data_saida__gte=datetime.now())

    noticias = NoticiaTimes.objects.filter(publicar__icontains=1,
                                           time__slugtime=slugtime).order_by('-datapublicacao')

    team = get_object_or_404(Times, slugtime=slugtime)
    teams = Times.objects.all().order_by('-nome')

    categorias = CategoriaNoticia.objects.all().order_by('nome')
    subcategorias = SubCategoria.objects.all().order_by('nome')

    return render_to_response('igenius/time-home.html', locals(), context_instance=RequestContext(request))


def timemais(request, slugtime):
    lidas = Noticia.objects.filter(publicar__icontains=1).order_by('-hits')[:7]

    blogs = BlogUsuario.objects.all().order_by('-blog')
    publicidade = Publicidade.objects.filter(data_entrada__lte=datetime.now(), data_saida__gte=datetime.now())

    noticias = NoticiaTimes.objects.filter(publicar__icontains=1,
                                           time__slugtime=slugtime).order_by('-datapublicacao')

    team = get_object_or_404(Times, slugtime=slugtime)
    teams = Times.objects.all().order_by('-nome')

    categorias = CategoriaNoticia.objects.all().order_by('nome')
    subcategorias = SubCategoria.objects.all().order_by('nome')

    return render_to_response('igenius/time-home-mais.html', locals(), context_instance=RequestContext(request))


def subcategoria(request, slugcategoria, slugsubcategoria):
    plantao = Noticia.objects.filter(publicar__icontains=1).order_by('-datapublicacao')[:7]

    lidas = Noticia.objects.filter(publicar__icontains=1, subcategoria__categoria__slugcategoria=slugcategoria,
                                   subcategoria__slugsubcategoria=slugsubcategoria).order_by('-hits')[:7]
    blogs = BlogUsuario.objects.all().order_by('-blog')
    publicidade = Publicidade.objects.filter(data_entrada__lte=datetime.now(), data_saida__gte=datetime.now())
    team = Times.objects.all().order_by('-nome')

    noticias = Noticia.objects.filter(manchete__icontains=0, publicar__icontains=1,
                                      subcategoria__categoria__slugcategoria=slugcategoria,
                                      subcategoria__slugsubcategoria=slugsubcategoria).order_by('-datapublicacao')

    cat = get_object_or_404(CategoriaNoticia, slugcategoria__contains=slugcategoria)
    subcat = get_object_or_404(SubCategoria, slugsubcategoria=slugsubcategoria)
    subcategoria = SubCategoria.objects.filter(categoria__slugcategoria__contains=slugcategoria).order_by('nome')[:8]

    categorias = CategoriaNoticia.objects.all().order_by('nome')
    subcategorias = SubCategoria.objects.all().order_by('nome')

    return render_to_response('igenius/sub-categoria-home.html', locals(), context_instance=RequestContext(request))


def noticiatime(request, slugcategoria, slugsubcategoria, slugtime, slugnoticia):
    plantao = Noticia.objects.filter(publicar__icontains=1).order_by('-datapublicacao')[:7]

    lidas = Noticia.objects.filter(publicar__icontains=1, subcategoria__categoria__slugcategoria=slugcategoria,
                                   subcategoria__slugsubcategoria=slugsubcategoria).order_by('-hits')[:7]
    blogs = BlogUsuario.objects.all().order_by('-blog')
    publicidade = Publicidade.objects.filter(data_entrada__lte=datetime.now(), data_saida__gte=datetime.now())
    team = Times.objects.all().order_by('-nome')

    noticia = get_object_or_404(NoticiaTimes, subcategoria__categoria__slugcategoria=slugcategoria,
                                subcategoria__slugsubcategoria=slugsubcategoria, time__slugtime=slugtime,
                                slugnoticia=slugnoticia)

    noticias = Noticia.objects.filter(manchete__icontains=0, publicar__icontains=1,
                                      subcategoria__categoria__slugcategoria=slugcategoria,
                                      subcategoria__slugsubcategoria=slugsubcategoria).order_by('-datapublicacao')

    cat = get_object_or_404(CategoriaNoticia, slugcategoria__contains=slugcategoria)
    subcat = get_object_or_404(SubCategoria, slugsubcategoria=slugsubcategoria)
    subcategoria = SubCategoria.objects.filter(categoria__slugcategoria__contains=slugcategoria).order_by('-nome')

    categorias = CategoriaNoticia.objects.all().order_by('nome')
    subcategorias = SubCategoria.objects.all().order_by('nome')

    return render_to_response('igenius/noticia-interna.html', locals(), context_instance=RequestContext(request))


def bloghome(request, slugblog):
    blogs = BlogUsuario.objects.filter(blog__ativo__icontains=1).order_by('-blog')
    publicidade = PublicidadeBlog.objects.filter(blog__slugblog=slugblog, data_entrada__lte=datetime.now(),
                                                 data_saida__gte=datetime.now())
    plantao = Noticia.objects.filter(publicar__icontains=1).order_by('-datapublicacao')

    noticiasblog = NoticiaBlog.objects.filter(publicar__icontains=1, blog__blog__slugblog=slugblog).order_by(
        '-criado_em')[:30]

    blog = get_object_or_404(Blog, ativo__icontains=1, slugblog=slugblog)
    dblog = get_object_or_404(BlogUsuario, blog__slugblog=slugblog)

    categorias = CategoriaNoticia.objects.all().order_by('nome')
    subcategorias = SubCategoria.objects.all().order_by('nome')

    return render_to_response('igenius/blog-home.html', locals(), context_instance=RequestContext(request))


def busca(request):
    lidas = Noticia.objects.filter(publicar__icontains=1).order_by('-hits')[:7]

    # noticias = Noticia.objects.filter(posicao__id__icontains = 5,publicar__icontains=1,manchete__icontains=0).order_by('-datapublicacao')[:9]
    blogs = BlogUsuario.objects.all().order_by('-blog')
    publicidade = Publicidade.objects.filter(data_entrada__lte=datetime.now(), data_saida__gte=datetime.now())

    from django.db.models.query_utils import Q

    quante = 0
    if request.GET['buscap'] != '':
        ites = Noticia.objects.filter(
            (Q(subtitulo__icontains=request.GET['buscap']) | Q(titulo__icontains=request.GET['buscap'])))
        if ites:
            quante = ites.count()
        c = Context({'itens_busca': ites, 'quant': quante, 'bus': request.GET['buscap']})

        return render_to_response('igenius/busca.html', locals(), context_instance=RequestContext(request, c))

    return render_to_response('igenius/index.html', locals(), context_instance=RequestContext(request, {
        'msg': 'Por Favor, preencha pelo menos um campo de busca!'}))


def buscablog(request):
    lidas = Noticia.objects.filter(publicar__icontains=1).order_by('-hits')[:7]


    # noticias = Noticia.objects.filter(posicao__id__icontains = 5,publicar__icontains=1,manchete__icontains=0).order_by('-datapublicacao')[:9]
    blogs = BlogUsuario.objects.all().order_by('-blog')
    publicidade = Publicidade.objects.filter(data_entrada__lte=datetime.now(), data_saida__gte=datetime.now())

    from django.db.models.query_utils import Q

    rblog = ''
    if request.GET['blog'] != '':
        rblog = request.GET['blog']

    blog = get_object_or_404(Blog, slugblog=rblog)
    dblog = get_object_or_404(BlogUsuario, blog__slugblog=rblog)

    categorias = CategoriaNoticia.objects.all().order_by('nome')
    subcategorias = SubCategoria.objects.all().order_by('nome')

    quante = 0
    if request.GET['buscab'] != '':
        ites = NoticiaBlog.objects.filter(
            (Q(subtitulo__icontains=request.GET['buscab']) | Q(titulo__icontains=request.GET['buscab'])),
            blog__blog__slugblog=rblog)
        if ites:
            quante = ites.count()
        c = Context({'itens_busca': ites, 'quant': quante, 'bus': request.GET['buscab']})

        return render_to_response('igenius/busca-blog.html', locals(), context_instance=RequestContext(request, c))

    return render_to_response('igenius/index.html', locals(), context_instance=RequestContext(request, {
        'msg': 'Por Favor, preencha pelo menos um campo de busca!'}))
