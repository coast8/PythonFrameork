# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.db.models import signals
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField

class BaseNoticia(models.Model):
    publicar = models.BooleanField(default=True)
    destaque = models.BooleanField(default=False)
    titulo = models.CharField('Titulo', max_length=100, unique=True)
    conteudo = RichTextField('Conteúdo', config_name='juniorlima')
    cliques = models.IntegerField('Cliques', default=0, editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, related_name='user_add_%(class)ss', blank=True, null=True, editable=False)
    usuario_modificou = models.ForeignKey(User, related_name='user_mod_%(class)ss', blank=True, null=True)
    class Meta:
        abstract = True


class Noticia(BaseNoticia):
    subtitulo = models.CharField('Subtitulo', max_length=200, blank=True, null=True)
    imagem = ImageField('Imagem Destaque', upload_to='noticia', blank=True, null=True)
    fonte = models.CharField(max_length=30, blank=True, null=True, help_text='Se essa notícia não é de sua autoria, insira o site original dela.')
    slug = models.SlugField(max_length=100, blank=True, unique=True, editable=False)
    
    def __unicode__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('rest.views.noticia', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

# SIGNALS

def noticia_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)

signals.pre_save.connect(noticia_pre_save, sender=Noticia)