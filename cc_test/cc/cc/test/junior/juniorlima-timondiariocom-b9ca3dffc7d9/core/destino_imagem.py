__author__ = 'Junior Lima'

def administrativo_empresa(instance, filename):
    return '/'.join(['administrativo/empresa', filename])

def administrativo_colaborador(instance, filename):
    return '/'.join(['administrativo/colaborador', filename])

def blog_blog(instance, filename):
    return '/'.join(['blogs', str(instance.slugblog), filename])

def blog_noticia(instance, filename):
    return '/'.join(['blogs', str(instance.blog.blog.slugblog), filename])

def campeonato_jogador(instance, filename):
    return '/'.join(['campeonato', str(instance.time_nome.campeonato_nome.ano), str(instance.time_nome.campeonato_nome.slugcampeonato), str(instance.time_nome.slugtime), filename])

from django.template.defaultfilters import slugify
from os.path import splitext, split, join
def letra_cantor(instance, filename):
    path, file_name = split(filename)
    file_name, ext = splitext(file_name)
    return '/'.join(['album/', str(instance.slugcantor), 'capa', slugify(instance.nome)+ext])
    #return '/'.join(['path/', slugify(file_name)+ext])
    #return '/'.join(['album', str(instance.slugcantor), 'capa', filename])

def local_local(instance, filename):
    return '/'.join(['local', str(instance.cidade_uf.slugcidade), filename])

def noticia_noticia(instance, filename):
    return '/'.join(['noticia', str(instance.categoria_nome.slugcategoria), filename])

def noticia_album(instance, filename):
    path, file_name = split(filename)
    file_name, ext = splitext(file_name)
    novo_filename = '%s-%s' % (instance.cantor_nome.slugcantor, slugify(instance.titulo)+ext)
    print novo_filename
    return '/'.join(['album', str(instance.cantor_nome.slugcantor), novo_filename])

def galeria_album(instance, filename):
    return '/'.join(['fotos', str(instance.slug), 'capa', filename])