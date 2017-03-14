# -*- coding: utf-8 -*-
from django.utils.datetime_safe import datetime

__author__ = 'Junior Lima'

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from core.models import BaseNoticiaVideo
from core.destino_imagem import blog_blog, blog_noticia
from core.thumbs import ImageWithThumbsField
from lib.ckeditor.fields import RichTextField
from igenius.models import Colaborador
from noticias.models import Noticia

COR_CHOICES = (('azul','Azul'),('bege','Bege'),('rosa','Rosa'),('verde','Verde'))

class BlogCategoria(models.Model):
    """ Este modelo descreve a categoria de blogs """
    ativo = models.BooleanField(default=True)
    nome = models.CharField(max_length=30, unique=True)
    descricao = models.CharField(max_length=100,blank=True)
    criado_em = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Blogs - Categoria'
        verbose_name_plural = 'Blogs - Categorias'
    def __unicode__(self):
        return self.nome


class Blog(models.Model):
    """ Este modelo descreve os blogs """
    ativo = models.BooleanField(default=True)
    nome = models.CharField(max_length=25, unique=True)

    cor = models.CharField(choices=COR_CHOICES,max_length=200, blank=True, null=True)

    email = models.CharField('Email do Blog', max_length=50, blank=True, null=True)

    resumo = models.CharField('Chamada do blog', max_length=20, blank=True, null=True)
    descricao = models.CharField(max_length=200, blank=True, null=True, help_text='Adicione uma descrição objetiva. Ela será mostrada quando seu blog for pesquisado no Google')

    imagem_capa = ImageWithThumbsField('Imagem Destaque', upload_to=blog_blog, sizes=((800,600),(300,225)), blank=True, null=True)
    imagem_extra = ImageWithThumbsField('Imagem Destaque', upload_to=blog_blog, sizes=((800,600),(300,225)), blank=True, null=True)

    categoria_nome = models.ForeignKey(BlogCategoria, blank=True, null=True)

    slugblog = models.SlugField(max_length=255, blank=True, unique=True, editable=False)
    cliques = models.IntegerField('Cliques', default=0, editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    #usuario = models.ForeignKey(User, blank=True, null=True)
    colaborador = models.ForeignKey(Colaborador)

    def __unicode__(self):
        return self.nome
    def get_absolute_url(self):
        return reverse('igenius.views.bloghome', kwargs={'slugblog': self.slugblog})
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

class BlogUsuario(models.Model):
    blog = models.ForeignKey(Blog, related_name='blog_usuario_set')
    usuario = models.ForeignKey(User)
    colaborador = models.ForeignKey(Colaborador)
    unique_together = (("blog", "usuario"),)
    def __unicode__(self):
        return '%s %s' % (self.blog.nome, self.usuario.username)
    def nome_usuario(self):
        return self.usuario.get_full_name()
    def categoria_blog(self):
        return self.blog.categoria_nome.nome
    categoria_blog.short_description = ('Categoria')
    class Meta:
        verbose_name = 'Blogs - Usuário'
        verbose_name_plural = 'Blogs - Usuários'

class NoticiaBlog(models.Model):
    publicar = models.BooleanField(default=True)
    destaque = models.BooleanField(default=False)
    titulo = models.CharField(max_length=100)
    conteudo = RichTextField('Conteúdo', config_name='junior')
    slug = models.SlugField(max_length=150, blank=True, editable=False)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    cliques = models.IntegerField('Cliques', default=0, editable=False)

    usuario = models.ForeignKey(User, related_name='user_add_%(class)ss', blank=True, null=True)
    usuario_modificou = models.ForeignKey(User, related_name='user_mod_%(class)ss', blank=True, null=True)

    subtitulo = models.CharField(max_length=200, blank=True, null=True)
    fonte = models.CharField(max_length=30, blank=True, null=True)
    imagem = ImageWithThumbsField('Imagem Destaque', upload_to=blog_noticia, sizes=((800,600),(200,150)))
    blog = models.ForeignKey(BlogUsuario, verbose_name='Blog')
    unique_together = (("titulo", "blog"),)
    class Meta:
        verbose_name = 'notícia no blog'
        verbose_name_plural = 'Notícias no blog'
        ordering = ['-criado_em']
    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('igenius.views.noticiablog', kwargs={'slugblog': self.blog.blog.slugblog, 'slug': self.slug,})

class NoticiaBlogVideo(BaseNoticiaVideo):
    video_noticiablog = models.ForeignKey(NoticiaBlog)
    class Meta:
        verbose_name = 'vídeo na notícia'
        verbose_name_plural = 'Inserir vídeo na notícia'

PUBLICIDADE_CHOICES = (('1', 'Bloco Esquerda'),('2', 'Banner Extra'),('3', 'Interna Bloco'),('4', 'Barra fixa lateral'),('5', 'Quadrado'),('6', 'Interna Sidebar'),('7', 'Home Sidebar'))

class PublicidadeBlog(models.Model):
    ativo = models.BooleanField('Status',default=True)
    blog = models.ForeignKey(Blog)
    nome=models.CharField("Nome",max_length=100)
    valor = models.FloatField(blank=True, null=True)
    valorEntrada = models.FloatField(blank=True, null=True)
    valorFinal = models.FloatField(blank=True, null=True, editable=False)
    arquivo = models.FileField(upload_to='Publicidade')
    data_entrada=models.DateTimeField("Data de entrada",default=datetime.now)
    data_saida=models.DateTimeField("Data de saída")
    tipo=models.CharField('Tipo da publicidade', max_length=2, choices = PUBLICIDADE_CHOICES)
    url=models.URLField("Site da publicidade", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Inserir Publicidades Blog"

    def __unicode__(self):
        return self.nome

    def Final(self):
        r = (self.valor - self.valorEntrada)
        self.valorFinal.real = r
        self.save(self)
        return r


from django.db.models import signals
from django.template.defaultfilters import slugify

def blog_pre_save(signal, instance, sender, **kwargs):
    if not instance.slugblog:
        instance.slugblog = slugify(instance.nome)

signals.pre_save.connect(blog_pre_save, sender=Blog)

def noticiablog_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.titulo)

signals.pre_save.connect(noticiablog_pre_save, sender=NoticiaBlog)