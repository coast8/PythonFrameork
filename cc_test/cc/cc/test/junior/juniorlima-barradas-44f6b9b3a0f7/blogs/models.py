# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

import datetime
now = datetime.datetime.now()

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models import signals
from django.template.defaultfilters import slugify

from easy_thumbnails.fields import ThumbnailerImageField

from core.choices import COLOR_CSS_CHOICES
from portal.models import Noticia

class Blog(models.Model):
    """ Este modelo descreve os blogs """
    ativo = models.BooleanField(default=True)
    nome = models.CharField(max_length=25, unique=True)

    igreja = models.CharField('Dados Adicionais', max_length=50, blank=True, null=True)
    color = models.CharField('Atributo de cor',blank=True, null=True, max_length=20, choices=COLOR_CSS_CHOICES)
    email = models.CharField('Email do Blog', max_length=50)

    resumo = models.CharField('Chamada do blog', max_length=20)
    descricao = models.CharField(max_length=200, blank=True, null=True, help_text='Adicione uma descrição objetiva. Ela será sua apresentação na página do município')

    imagem_capa = ThumbnailerImageField('Foto do blogueiro', upload_to='blog',)
    imagem_extra = ThumbnailerImageField("Imagem de Capa do Blog", upload_to='blog', help_text='Tamanho recomendado: 1030x200', blank=True, null=True)

    slug = models.SlugField(max_length=255, blank=True, unique=True, editable=False)
    cliques = models.IntegerField('Cliques', default=0, editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, blank=True, null=True)
    def __unicode__(self):
        return self.nome
    def get_absolute_url(self):
        return reverse('portal.views.blog', kwargs={'slug': self.slug})
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
    imagem = ThumbnailerImageField('Imagem Destaque', upload_to='blog_noticia', blank=True, null=True)
    blog = models.ForeignKey(BlogUsuario, verbose_name='Blog')
    unique_together = (("titulo", "blog"),)
    class Meta:
        verbose_name = 'notícia no blog'
        verbose_name_plural = 'Notícias no blog'
    def get_next(self):
        next = NoticiaBlog.objects.filter(id__gt=self.id)
        if next:
            return next[0]
        return ''

    def get_prev(self):
        prev = NoticiaBlog.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev[0]
        return ''
    def __unicode__(self):
        return self.titulo
    def get_absolute_url(self):
        return reverse('portal.views.noticia_blog', kwargs={'blog': self.blog.blog.slug,
                                                            'slug': self.slug,})

# SIGNALS
def postagem_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)

signals.pre_save.connect(postagem_pre_save, sender=NoticiaBlog)

def blog_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(blog_pre_save, sender=Blog)
