# -*- coding: utf-8 -*-
__author__ = 'Junior'
from datetime import datetime
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.db import models
from django.core.urlresolvers import reverse
from igenius.thumbs import ImageWithThumbsField

from lib.ckeditor.fields import RichTextField
from lib.tagging_autocomplete.models import TagAutocompleteField
from igenius.models import Posicao,CategoriaNoticia,Colaborador,SubCategoria,Fonte
from noticias.models import *

def content_image_name_times(instance, filename):
    return '/'.join(['times', str(instance.slugtime),filename])

class Local(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)
    sluglocal = models.SlugField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Cadastrar Local"
        verbose_name_plural = "Cadastrar Locais"

    def __unicode__(self):
        return self.nome

class Campeonato(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    local = models.ForeignKey(Local)
    escudo = ImageWithThumbsField(verbose_name='Escudos Times', upload_to=content_image_name_times, sizes=((143,96),(291,165),(73,73),(400,260),(800,600)),blank=True,null=True)
    descricao = models.TextField(blank=True,null=True)
    slugcampeonato = models.SlugField(max_length=200,blank=True,null=True)


    class Meta:
       verbose_name = "Cadastrar Campeonato"
       verbose_name_plural = "Cadastrar Campeonatos"

    def __unicode__(self):
        return self.nome

class Cores(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True,null=True)
    slugcor = models.SlugField(max_length=200,blank=True,null=True)

    class Meta:
       verbose_name = "Cadastrar Cor"
       verbose_name_plural = "Cadastrar Cores"

    def __unicode__(self):
        return self.nome

class Times(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    cor = models.ForeignKey(Cores,verbose_name='Cor Time')
    site = models.URLField(blank=True, null=True)
    historia = models.TextField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    escudo = ImageWithThumbsField(verbose_name='Escudos Times', upload_to=content_image_name_times, sizes=((143,96),(291,165),(73,73),(400,260),(800,600)))
    slugtime = models.SlugField(max_length=200, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('igenius.views.timeInterna', kwargs={'slugtime':self.slugtime})

    class Meta:
       verbose_name_plural = "Cadastrar Times"

    def __unicode__(self):
        return self.nome

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

def cor_pre_save(signal, instance, sender, **kwargs):
    instance.slugcor = slugify(instance.nome)
signals.pre_save.connect(cor_pre_save, sender=Cores)

def time_pre_save(signal, instance, sender, **kwargs):
    instance.slugtime = slugify(instance.nome)
signals.pre_save.connect(time_pre_save, sender=Times)

def local_pre_save(signal, instance, sender, **kwargs):
    instance.sluglocal = slugify(instance.nome)
signals.pre_save.connect(local_pre_save, sender=Local)

def campeonato_pre_save(signal, instance, sender, **kwargs):
    instance.slugcampeonato = slugify(instance.nome)
signals.pre_save.connect(campeonato_pre_save, sender=Campeonato)