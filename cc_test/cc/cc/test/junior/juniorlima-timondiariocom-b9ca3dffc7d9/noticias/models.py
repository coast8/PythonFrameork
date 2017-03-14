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
from igenius.models import *
from times.models import Times,Campeonato
from lib.tagging.models import Tag

def content_image_name_noticia(instance, filename):
    return '/'.join(['noticias', str(instance.subcategoria.categoria.slugcategoria),str(instance.subcategoria.slugsubcategoria),filename])

def content_image_name_times(instance, filename):
    return '/'.join(['times', str(instance.slugtime),filename])


class Noticia(models.Model):
    aprovar = models.IntegerField(default=0)
    publicar = models.BooleanField(default=True)
    manchete = models.BooleanField('Manchete',default=False)
    titulo = models.CharField(max_length=100, unique=True)
    subtitulo = models.CharField(max_length=200)
    subcategoria = models.ForeignKey(SubCategoria)
    chamada = models.CharField(max_length=50, blank=True, null=True)
    conteudo = RichTextField('Conteúdo', config_name='junior')
    posicao = models.ForeignKey(Posicao,blank=True, null=True)
    datapublicacao = models.DateTimeField(auto_now_add=True)
    fonte = models.ForeignKey(Fonte)
    link = models.URLField('Link Fonte',blank=True,null=True)
    imagemDestaque = ImageWithThumbsField(verbose_name='Imagem Destaque', upload_to=content_image_name_noticia, sizes=((143,96),(383,155),(291,165),(73,73),(400,260),(800,600)))
    usarVideo = models.BooleanField('Usar Vídeo?',default=False)
    video = models.CharField('Link Vídeo',max_length=15, help_text="Vc_z2BZBLj4",blank=True,null=True)
    slugnoticia = models.SlugField(max_length=200, blank=True, unique=True)
    autor = models.ForeignKey(Colaborador)
    hits = models.IntegerField('Cliques', default=0, editable=False)
    tag = TagAutocompleteField('Assunto')
    extra = models.BooleanField('Extra',default=False)

    class Meta:
        verbose_name_plural = "Cadastrar Notícia"

    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('igenius.views.noticiainterna', kwargs={'slugcategoria':self.subcategoria.categoria.slugcategoria,'slugsubcategoria':self.subcategoria.slugsubcategoria,'slugnoticia': self.slugnoticia})

    def get_tags(self):
        return Tag.objects.get_for_object(self)

class NoticiaLocal(Noticia):
    bairro = models.ForeignKey(Bairros)

    class Meta:
        verbose_name_plural = "Cadastrar Notícia Local"

    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('igenius.views.noticiainternalocal', kwargs={'slugcategoria':self.subcategoria.categoria.slugcategoria,'slugsubcategoria':self.subcategoria.slugsubcategoria,'slugbairro':self.bairro.slugbairro,'slugnoticia': self.slugnoticia})

class NoticiaTimes(Noticia):
    time = models.ForeignKey(Times)
    campeonato = models.ForeignKey(Campeonato)

    class Meta:
        verbose_name = "Notícia Time"
        verbose_name_plural = "Notícias Times"

    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('igenius.views.noticiatime', kwargs={'slugcategoria':self.subcategoria.categoria.slugcategoria,'slugsubcategoria':self.subcategoria.slugsubcategoria,'slugtime':self.time.slugtime,'slugnoticia': self.slugnoticia})


# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

def noticia_pre_save(signal, instance, sender, **kwargs):
    if not instance.slugnoticia:
        slug = slugify(instance.titulo)
        novaslug = slug
        contador = 0

        while Noticia.objects.filter(slugnoticia = novaslug).exclude(id=instance.id).count() > 0:
            contador += 1
            novaslug = '%s-%d'%(slug, contador)
        instance.slugnoticia = novaslug

signals.pre_save.connect(noticia_pre_save, sender=Noticia)

def noticia_local_pre_save(signal, instance, sender, **kwargs):
    if not instance.slugnoticia:
        slug = slugify(instance.titulo)
        novaslug = slug
        contador = 0

        while Noticia.objects.filter(slugnoticia = novaslug).exclude(id=instance.id).count() > 0:
            contador += 1
            novaslug = '%s-%d'%(slug, contador)
        instance.slugnoticia = novaslug

signals.pre_save.connect(noticia_local_pre_save, sender=NoticiaLocal)

def noticia_times_local_pre_save(signal, instance, sender, **kwargs):
    if not instance.slugnoticia:
        slug = slugify(instance.titulo)
        novaslug = slug
        contador = 0

        while Noticia.objects.filter(slugnoticia = novaslug).exclude(id=instance.id).count() > 0:
            contador += 1
            novaslug = '%s-%d'%(slug, contador)
        instance.slugnoticia = novaslug

signals.pre_save.connect(noticia_times_local_pre_save, sender=NoticiaTimes)






