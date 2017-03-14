# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from core.models import Noticia, BaseNoticiaVideo
from core.destino_imagem import blog_blog, blog_noticia
from core.thumbs import ImageWithThumbsField

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

    igreja = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField('Email do Blog', max_length=50)

    resumo = models.CharField('Chamada do blog', max_length=20)
    descricao = models.CharField(max_length=200, blank=True, null=True, help_text='Adicione uma descrição objetiva. Ela será mostrada quando seu blog for pesquisado no Google')

    imagem_capa = ImageWithThumbsField('Imagem Destaque', upload_to=blog_blog, sizes=((800,600),(300,225)))
    imagem_extra = ImageWithThumbsField("Imagem de Capa do Blog", upload_to=blog_blog, sizes=((1030,200),(300,225)), help_text='Tamanho recomendado: 1030x200', blank=True, null=True)

    categoria_nome = models.ForeignKey(BlogCategoria)

    slugblog = models.SlugField(max_length=255, blank=True, unique=True, editable=False)
    cliques = models.IntegerField('Cliques', default=0, editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, blank=True, null=True)
    def __unicode__(self):
        return self.nome
    def get_absolute_url(self):
        return reverse('noticias.views.blog', kwargs={'nomedoblog': self.slugblog})
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

class BlogUsuario(models.Model):
    blog = models.ForeignKey(Blog, related_name='blog_usuario_set')
    usuario = models.ForeignKey(User)
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

class NoticiaBlog(Noticia):
    subtitulo = models.CharField(max_length=200, blank=True, null=True)
    fonte = models.CharField(max_length=30, blank=True, null=True)
    imagem = ImageWithThumbsField('Imagem Destaque', upload_to=blog_noticia, sizes=((800,600),(200,150)), blank=True, null=True)
    blog = models.ForeignKey(BlogUsuario, verbose_name='Blog')
    unique_together = (("titulo", "blog"),)
    class Meta:
        verbose_name = 'notícia no blog'
        verbose_name_plural = 'Notícias no blog'
        ordering = ['-criado_em']
    def __unicode__(self):
        return self.titulo
    def get_absolute_url(self):
        return reverse('noticias.views.noticiablog', kwargs={'slugblog': self.blog.blog.slugblog, 'slugnoticiablog': self.slug,})

class NoticiaBlogVideo(BaseNoticiaVideo):
    video_noticiablog = models.ForeignKey(NoticiaBlog)
    class Meta:
        verbose_name = 'vídeo na notícia'
        verbose_name_plural = 'Inserir vídeo na notícia'

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