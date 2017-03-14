# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from datetime import datetime
from django.template.context import RequestContext,Context
from django.shortcuts import render_to_response, get_object_or_404

from blogs.models import NoticiaBlog, Blog, BlogUsuario
from noticias.models import Noticias, Eventos, Album, VideoNoticia, Link, Categoria
from galeria.models import Galeria, FotoGaleria
from letras.models import Letra, Cantor, Genero
from locais.models import Local, Cidade, Estado
from shopping.models import Produto

def homepage(request):
    destaque = Noticias.objects.filter(destaque=True, publicar=True).order_by('-criado_em')[:5]
    noticias = Noticias.objects.filter(destaque=False, publicar=True, categoria_nome_id=6).order_by('-criado_em')[:5]
    humor = Noticias.objects.filter(destaque=False, publicar=True, categoria_nome_id=4).order_by('-criado_em')[:9]
    eventos = Eventos.objects.filter(evento_noticia__destaque=False, evento_noticia__publicar=True, dataevento__gte=datetime.now()).order_by('dataevento')[:5]
    galeriasfilter = Galeria.objects.filter(publicar=True, destaque=False).order_by('-criado_em')[:4]
    downloads = Album.objects.filter(destaque=False, publicar=True).order_by('-criado_em')[0:5]
    videos = VideoNoticia.objects.filter(video_noticia__publicar=True, video_noticia__destaque=False).order_by('-video_noticia__criado_em')[:7]
    cantores = Cantor.objects.filter(publicar=True).order_by('-criado_em')[:5]

    albuns = Album.objects.filter(destaque=False, publicar=True).order_by('-criado_em')[5:10]
    letras = Letra.objects.filter(destaque=False, publicar=True).order_by('-criado_em')[:5]
    destaquesblog = NoticiaBlog.objects.filter(destaque=False, publicar=True).order_by('-criado_em')[:7]
    artigos = Noticias.objects.filter(destaque=False, publicar=True, categoria_nome_id=1).order_by('-criado_em')[:7] #Artigos - 1

    return render_to_response('site/index.html',locals(),context_instance=RequestContext(request))

def blog(request, nomedoblog):
    blog = get_object_or_404(Blog, slugblog=nomedoblog, ativo=True)
    dono = BlogUsuario.objects.filter(blog=blog)
    noticias = NoticiaBlog.objects.filter(blog__blog=blog)
    return render_to_response('site/blog.html',locals(),context_instance=RequestContext(request))

def noticia(request, slugcategoria, slug):
    noticia = get_object_or_404(Noticias, categoria_nome__slugcategoria=slugcategoria, slug=slug, publicar=True)
    relacionados = Noticias.objects.filter(categoria_nome=noticia.categoria_nome).order_by('-criado_em')[:10]
    if noticia:
        if not request.session.get('noticia_cliques_%s' % slug):
            noticia.cliques = noticia.cliques + 1
            noticia.save()
            request.session['noticia_cliques_%s' % slug] = True
    if noticia.categoria_nome_id == 7:
        return render_to_response('juvenis/video.html',locals(),context_instance=RequestContext(request))
    else:
        return render_to_response('site/noticia.html',locals(),context_instance=RequestContext(request))

def noticiablog(request, slugblog, slugnoticiablog):
    noticia = get_object_or_404(NoticiaBlog, blog__blog__slugblog=slugblog, slug=slugnoticiablog, publicar=True)
    ultimas = NoticiaBlog.objects.filter(publicar=True).exclude(blog__blog=noticia.blog.blog).order_by('-criado_em')[:5]
    relacionadas = NoticiaBlog.objects.filter(blog__blog=noticia.blog.blog).exclude(pk=noticia.pk).order_by('-criado_em')[:5]
    if noticiablog:
        if not request.session.get('noticia_cliques_%s' % slugnoticiablog):
            noticia.cliques = noticia.cliques + 1
            noticia.save()
            request.session['noticia_cliques_%s' % slugnoticiablog] = True
    return render_to_response('site/noticia-blog.html',locals(),context_instance=RequestContext(request))

def categorianoticia(request, slugcategoria):
    categoria = get_object_or_404(Categoria, slugcategoria=slugcategoria, publicar=True)
    noticias_list = Noticias.objects.filter(categoria_nome__slugcategoria=categoria, publicar=True, destaque=False).order_by('-criado_em')
    if categoria.id == 3:
        proximos = noticias_list.filter(publicar=True, evento_noticia_set__dataevento__gte=datetime.now()).select_related().order_by('evento_noticia_set__dataevento')
        outros = noticias_list.exclude(id__in=proximos)
        return render_to_response('juvenis/categoria-eventos.html',locals(),context_instance=RequestContext(request))
    if categoria.id == 7:
        return render_to_response('juvenis/categoria-videos.html',locals(),context_instance=RequestContext(request))
    else:
        return render_to_response('juvenis/categoria.html',locals(),context_instance=RequestContext(request))

def ultimas(request):
    noticias = Noticias.objects.filter(publicar=True, destaque=False).order_by('-criado_em')
    return render_to_response('juvenis/ultimas.html',locals(),context_instance=RequestContext(request))

def evento_estado(request, slugestado):
    estado = get_object_or_404(Estado, sigla=slugestado)
    noticias = Eventos.objects.filter(cidade__uf=estado).order_by('-evento_noticia__criado_em')
    return render_to_response('juvenis/categoria-eventos-uf.html',locals(),context_instance=RequestContext(request))

def evento_cidade(request, slugestado, slugcidade):
    cidade = get_object_or_404(Cidade, uf__sigla=slugestado, slugcidade=slugcidade)
    noticias = Eventos.objects.filter(cidade__slugcidade=slugcidade).order_by('-evento_noticia__criado_em')
    return render_to_response('juvenis/categoria-eventos-ci.html',locals(),context_instance=RequestContext(request))

def evento(request, slugcategoria, slugestado, slugcidade, slug):
    noticia = get_object_or_404(Eventos, evento_noticia__categoria_nome__slugcategoria=slugcategoria, cidade__uf__sigla=slugestado, cidade__slugcidade=slugcidade, evento_noticia__slug=slug, evento_noticia__publicar=True)
    relacionados = Eventos.objects.filter(cidade__uf=noticia.cidade.uf, evento_noticia__publicar=True).exclude(pk=noticia.pk).order_by('-evento_noticia__criado_em')[:5]
    if noticia:
        if not request.session.get('noticia_evento_noticia_cliques_%s' % slug):
            noticia.evento_noticia.cliques = noticia.evento_noticia.cliques + 1
            noticia.evento_noticia.save()
            request.session['noticia_cliques_%s' % slug] = True

    return render_to_response('juvenis/noticia-evento.html',locals(),context_instance=RequestContext(request))



def blogs(request):
    blogs = Blog.objects.filter(ativo=True).order_by('-criado_em')
    return render_to_response('juvenis/blogs.html',locals(),context_instance=RequestContext(request))

def cantor(request, slugcantor):
    cantor = get_object_or_404(Cantor, slugcantor=slugcantor, publicar=True)
    return render_to_response('juvenis/cantor.html',locals(),context_instance=RequestContext(request))

def downloads(request):
    down_dest = Album.objects.filter(publicar=True)[0:4]
    down_rec = Album.objects.filter(publicar=True)[4:9]
    down_list = Album.objects.filter(publicar=True)[8:]
    return render_to_response('juvenis/categoria-dowloads.html',locals(),context_instance=RequestContext(request))

def downloadcantor(request, slugcantor):
    cantor = get_object_or_404(Cantor, slugcantor=slugcantor, publicar=True)
    download_list = Album.objects.filter(cantor_nome=cantor, publicar=True).order_by('-criado_em')
    return render_to_response('juvenis/download-cantor.html',locals(),context_instance=RequestContext(request))

def download(request, slugcantor, slugalbum):
    noticia = get_object_or_404(Album, cantor_nome__slugcantor=slugcantor, slug=slugalbum, publicar=True)
    letras = Letra.objects.filter(album_nome=noticia)
    relacionados = Album.objects.filter(cantor_nome=noticia.cantor_nome).exclude(slug=slugalbum)
    if noticia:
        if not request.session.get('noticia_cliques_%s' % slugalbum):
            noticia.cliques = noticia.cliques + 1
            noticia.save()
            request.session['noticia_cliques_%s' % slugalbum] = True
    return render_to_response('juvenis/noticia-download.html',locals(),context_instance=RequestContext(request))

def genero(request, sluggenero):
    genero = get_object_or_404(Genero, sluggenero=sluggenero, ativo=True)
    return render_to_response('juvenis/genero.html',locals(),context_instance=RequestContext(request))

def downloadlink(request, cantor_id, download_id):
    album = get_object_or_404(Album, cantor_nome_id=cantor_id, id=download_id, publicar=True)
    linkdownload = Link.objects.filter(link_downloadalbum=album)
    gostar = Album.objects.filter(cantor_nome__genero_nome__id__exact=album.cantor_nome.genero_nome.id).exclude(pk=album.pk).order_by('-criado_em')[:5]
    outros_cantor = Album.objects.filter(cantor_nome__id=album.cantor_nome.id).order_by('-criado_em')
    recents = Album.objects.filter(publicar=True).order_by('-criado_em')[:5]
    return render_to_response('juvenis/download-link.html',locals(),context_instance=RequestContext(request))

def locais(request):
    locais = Local.objects.filter(publicar=True)
    return render_to_response('juvenis/locais.html',locals(),context_instance=RequestContext(request))

def local(request, slugcidade, slugdolocal):
    noticia = get_object_or_404(Local, cidade_uf__slugcidade=slugcidade, sluglocal=slugdolocal)
    relacionados = Local.objects.filter(categoria_nome__id=noticia.categoria_nome.id, cidade_uf__id=noticia.cidade_uf.id).order_by('-cliques')[:5]
    if noticia:
        if not request.session.get('noticia_cliques_%s' % slugdolocal):
            noticia.cliques = noticia.cliques + 1
            noticia.save()
            request.session['noticia_cliques_%s' % slugdolocal] = True
    return render_to_response('juvenis/local.html',locals(),context_instance=RequestContext(request))

def produtos(request):
    produtos = Produto.objects.filter(publicar=True)
    return render_to_response('juvenis/produtos.html',locals(),context_instance=RequestContext(request))

def produto(request, slugcategoria, slugproduto):
    produto = get_object_or_404(Produto, categoria_nome__slugcatproduto=slugcategoria, slug=slugproduto, publicar=True)
    return render_to_response('juvenis/produto.html',locals(),context_instance=RequestContext(request))

def galerias(request):
    galeriasfilter = Galeria.objects.filter(publicar=True).order_by('-criado_em')
    return render_to_response('juvenis/galerias.html',locals(),context_instance=RequestContext(request))

def galeria(request, sluggaleria):
    noticia = get_object_or_404(Galeria, slug=sluggaleria, publicar=True)
    fotos = FotoGaleria.objects.filter(galeria=noticia)
    ultimas = Galeria.objects.exclude(slug=sluggaleria).filter(publicar=True).order_by('-criado_em')[:5]
    return render_to_response('juvenis/galeria.html',locals(),context_instance=RequestContext(request))

def foto(request, galeria_id, foto_id):
    foto = get_object_or_404(FotoGaleria, galeria_id=galeria_id, id=foto_id)
    ultimas = Galeria.objects.exclude(id=galeria_id).filter(publicar=True).order_by('-criado_em')[:5]
    if foto:
        if not request.session.get('noticia_cliques_%s' % foto_id):
            foto.cliques = foto.cliques + 1
            foto.save()
            request.session['noticia_cliques_%s' % foto_id] = True
    return render_to_response('juvenis/foto.html',locals(),context_instance=RequestContext(request))

def letras(request):
    letras_destaque = Letra.objects.filter(publicar=True, destaque=True).order_by('-criado_em')[:5]
    cantor = Cantor.objects.filter(publicar=True).order_by('-criado_em')[:5]
    music_list = Noticias.objects.filter(publicar=True, categoria_nome__id=5).order_by('-criado_em')[:5]
    letra_recent = Letra.objects.filter(publicar=True).order_by('-criado_em')[5:55]
    return render_to_response('juvenis/letras-inicial.html',locals(),context_instance=RequestContext(request))

def letracantor(request, slugcantor):
    cantor = get_object_or_404(Cantor, slugcantor=slugcantor, publicar=True)
    letra_list = Letra.objects.filter(album_nome__cantor_nome=cantor, publicar=True).order_by('-cliques')
    return render_to_response('juvenis/letra-cantor.html',locals(),context_instance=RequestContext(request))

def letra(request, slugcantor, slugletra):
    letra = get_object_or_404(Letra, album_nome__cantor_nome__slugcantor=slugcantor, slug=slugletra, publicar=True)
    relacionados = Letra.objects.filter(album_nome__cantor_nome=letra.album_nome.cantor_nome).exclude(pk=letra.pk).order_by('-criado_em')
    musicas = Noticias.objects.filter(categoria_nome__id__exact=5, publicar=True).order_by('-criado_em')[:5]
    if letra:
        if not request.session.get('letra_cliques_%s' % slugletra):
            letra.cliques = letra.cliques + 1
            letra.save()
            request.session['noticia_cliques_%s' % slugletra] = True
    return render_to_response('juvenis/letra.html',locals(),context_instance=RequestContext(request))


def contato(request):
    return render_to_response('juvenis/contato.html',locals(),context_instance=RequestContext(request))

def erro(request):
    noticias = Noticias.objects.filter(publicar=True).order_by('-criado_em')[:8]
    return render_to_response('juvenis/404.html',locals(),context_instance=RequestContext(request))

def searchp(request):
    from django.db.models.query_utils import Q
    quante = 0
    if request.GET['searchp']!='' :
        noti = Noticias.objects.filter((Q(subtitulo__icontains = request.GET['searchp'])| Q(titulo__icontains = request.GET['searchp'])))
        down = Album.objects.filter((Q(titulo__icontains = request.GET['searchp'])| Q(cantor_nome__nome__icontains = request.GET['searchp'])))
        ites = list(down) + list(noti)
        if ites:
            c = Context({'itens_busca': ites, 'bus':request.GET['searchp']})
        return render_to_response('juvenis/busca.html', locals() ,context_instance=RequestContext(request,c))


    return render_to_response('juvenis/index.html', locals() ,context_instance=RequestContext(request,{'msg':'Por Favor, preencha pelo menos um campo de busca!'}))