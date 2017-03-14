from __future__ import unicode_literals
# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.sitemaps import ping_google
from filer.fields.image import FilerImageField
from django.core.exceptions import ValidationError

import datetime

from easy_thumbnails.fields import ThumbnailerImageField
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    publicar = models.BooleanField(default=True)
    nome = models.CharField(max_length=30)
    descricao = models.TextField(blank=True, null=True)
    cliques = models.IntegerField('Cliques', default=0, editable=False)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    class Meta:
        verbose_name_plural = 'Categoria de notícias'
        ordering = ['id']
    def __unicode__(self):
        return self.nome
    def get_absolute_url(self):
        return reverse('assessoria.views.categoria', kwargs={'slugcategoria': self.slug})

class Postagem(models.Model):
    publicar = models.BooleanField('Publicar', default=True)
    destaque = models.BooleanField('Destaque', default=True)
    titulo = models.CharField('Título', max_length=100, unique=True)
    subtitulo = models.CharField('Subtítulo', max_length=200)
    conteudo = RichTextField('Conteúdo', config_name='junior_lima')

    #posicao_foto = models.CharField('Posição da foto', max_length=2, choices=BLOG_POSTAGEM_POSICAO, default='1')
    imagem = ThumbnailerImageField(upload_to='imagens', blank=True)
    imagem_disco = FilerImageField(null=True, blank=True, related_name="imagem_noticia")

    categoria = models.ForeignKey(Categoria)
    slug = models.SlugField(max_length=110, unique=True, blank=True, null=True)
    cliques = models.IntegerField('Cliques', default=0, editable=False)
    data_publicacao = models.DateTimeField('Data de publicação', default=datetime.datetime.now())
    data_atualizacao = models.DateTimeField('Data de publicação', auto_now=True)
    usuario = models.ForeignKey(User, related_name='usuario_add', blank=True, null=True)
    usuario_modificou = models.ForeignKey(User, related_name='usuario_mod', blank=True, null=True)
    def __unicode__(self):
        return self.titulo
    def img(self):
        if self.imagem:
            return self.imagem
        elif self.imagem_disco:
            return self.imagem_disco
        else:
            None
    def get_absolute_url(self):
        return reverse('portal:noticia', kwargs={'slugcategoria': self.categoria.slug,
                                                 'slug': self.slug
                                                 })
    def save(self, force_insert=False, force_update=False):
        super(Postagem, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            pass
    def clean(self):
        if not self.id:
            if self.destaque==1 and self.imagem is None:
                raise ValidationError('Favor, faça o upload de uma imagem')
    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'



from django.db.models import signals
from django.template.defaultfilters import slugify

def categoria_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.nome)

signals.pre_save.connect(categoria_pre_save, sender=Categoria)

def postagem_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.titulo)

signals.pre_save.connect(postagem_pre_save, sender=Postagem)