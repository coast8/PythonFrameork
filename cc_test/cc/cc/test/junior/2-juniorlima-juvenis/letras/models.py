# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from noticias.models import Album
from core.models import BaseNoticiaAbstract
from core.destino_imagem import letra_cantor
from core.thumbs import ImageWithThumbsField
#Download
class Genero(models.Model):
    ativo = models.BooleanField(default=True)
    nome = models.CharField('Gênero musical', max_length=50, unique=True)
    cliques = models.IntegerField('Cliques', default=0, editable=False)
    sluggenero = models.SlugField(max_length=50, blank=True, unique=True)
    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name_plural = 'Gênero'
    def get_absolute_url(self):
        return reverse('noticias.views.genero', kwargs={'sluggenero': self.sluggenero})

class Cantor(models.Model):
    publicar = models.BooleanField(default=True)
    destaque = models.BooleanField(default=False)
    inicial = models.BooleanField(default=False)
    adsense = models.BooleanField(default=True)

    nome = models.CharField('Nome do cantor', max_length=50, unique=True)
    genero_nome = models.ForeignKey(Genero)

    descricao = models.TextField(blank=True, null=True)

    foto01 = ImageWithThumbsField('Foto', upload_to=letra_cantor, sizes=((800,600),(300,225),(100,75)))
    foto02 = ImageWithThumbsField('Foto', upload_to=letra_cantor, sizes=((800,600),(300,225)), blank=True, null=True)
    foto03 = ImageWithThumbsField('Foto', upload_to=letra_cantor, sizes=((800,600),(300,225)), blank=True, null=True)

    siteoficial = models.URLField('Site Oficial', max_length=50, blank=True, null=True)
    cliques = models.IntegerField('Cliques', default=0, editable=False)
    slugcantor = models.SlugField(max_length=50, blank=True, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    hora_album = models.DateTimeField(auto_now=True)
    cliques = models.IntegerField('Cliques', default=0, editable=False)
    usuario = models.ForeignKey(User, related_name='user_add_%(class)ss', blank=True, null=True)
    usuario_modificou = models.ForeignKey(User, related_name='user_mod_%(class)ss', blank=True, null=True)
    def __unicode__(self):
        return self.nome
    def letra_cantor_url(self):
        return reverse('noticias.views.letracantor', kwargs={'slugcantor': self.slugcantor})
    def download_cantor_url(self):
        return reverse('noticias.views.downloadcantor', kwargs={'slugcantor': self.slugcantor})
    class Meta:
        verbose_name_plural = 'Cantores'

#Letra
class Letra(BaseNoticiaAbstract):
    album_nome = models.ForeignKey(Album, verbose_name='Album')
    urlvideo = models.CharField(max_length=15, help_text="fhbTBA64FkU", blank=True, null=True)
    def get_absolute_url(self):
        return reverse('noticias.views.letra', kwargs={'slugcantor':self.album_nome.cantor_nome.slugcantor,
                                                       'slugletra': self.slug
        })
    def __unicode__(self):
        return  self.titulo
    class Meta:
        verbose_name = 'Letra'
        verbose_name_plural = 'Letras'
        unique_together = ("titulo", "album_nome")



from django.db.models import signals
from django.template.defaultfilters import slugify
def letra_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.titulo)
signals.pre_save.connect(letra_pre_save, sender=Letra)

def genero_pre_save(signal, instance, sender, **kwargs):
    instance.sluggenero = slugify(instance.nome)
signals.pre_save.connect(genero_pre_save, sender=Genero)

def cantor_pre_save(signal, instance, sender, **kwargs):
    instance.slugcantor = slugify(instance.nome)
signals.pre_save.connect(cantor_pre_save, sender=Cantor)
