from __future__ import unicode_literals
# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from ckeditor.fields import RichTextField
from easy_thumbnails.fields import ThumbnailerImageField

from django.contrib.auth.models import User
from django.db import models

class Categoria(models.Model):
    ativo = models.BooleanField(default=True)
    nome = models.CharField('Nome', max_length=50, unique=True)
    descricao = models.CharField('Nome', max_length=200, default='Descricao')
    slug = models.SlugField(max_length=60, blank=True)
    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Marca(models.Model):
    ativo = models.BooleanField(default=True)
    nome = models.CharField('Nome', max_length=50, unique=True)
    informacoes = RichTextField('Informações', config_name='junior_lima', default='Descricao')
    documento = models.FileField('Documento',blank=True, null=True)
    slug = models.SlugField(max_length=60, blank=True)
    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marca'

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=50, unique=True)
    marca = models.ForeignKey(Marca)
    categoria = models.ForeignKey(Categoria)
    informacoes = RichTextField('Informações', config_name='junior_lima')
    imagem = ThumbnailerImageField(upload_to='imagens', blank=True)
    slug = models.SlugField(max_length=60, blank=True)
    usuario = models.ForeignKey(User, related_name='user_add_%(class)ss', blank=True, null=True, editable=False)
    usuario_modificou = models.ForeignKey(User, related_name='user_mod_%(class)ss', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return "%s" % (self.nome)

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

def categoria_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        slug = slugify(instance.nome)
        novo_slug = slug
        contador = 0
        while Categoria.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
            contador += 1
            novo_slug = '%s-%d'%(slug, contador)
        instance.slug = novo_slug

signals.pre_save.connect(categoria_pre_save, sender=Categoria)

def marca_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        slug = slugify(instance.nome)
        novo_slug = slug
        contador = 0
        while Marca.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
            contador += 1
            novo_slug = '%s-%d'%(slug, contador)
        instance.slug = novo_slug

signals.pre_save.connect(marca_pre_save, sender=Marca)

def produto_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        slug = slugify(instance.nome)
        novo_slug = slug
        contador = 0
        while Produto.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
            contador += 1
            novo_slug = '%s-%d'%(slug, contador)
        instance.slug = novo_slug

signals.pre_save.connect(produto_pre_save, sender=Produto)