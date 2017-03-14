# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.db import models
from django.contrib.sitemaps import ping_google
from django.core.urlresolvers import reverse
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from easy_thumbnails.fields import ThumbnailerImageField
from ckeditor.fields import RichTextField


# Categoria de notícias
class Categoria(models.Model):
    publicar = models.BooleanField(default=True)
    nome = models.CharField(max_length=30)
    descricao = models.TextField(blank=True, null=True)
    cliques = models.IntegerField('Cliques', default=0, editable=False)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    class Meta:
        verbose_name_plural = 'Categoria de notícias'
    def __unicode__(self):
        return self.nome
    def get_absolute_url(self):
        return reverse('noticias.views.categorianoticia', kwargs={'slugcategoria': self.slug})

class Postagem(models.Model):
    publicar = models.BooleanField('Publicar', default=True)
    destaque = models.BooleanField('Destaque', default=False)
    titulo = models.CharField('Título', max_length=100, unique=True)
    subtitulo = models.CharField('Subtítulo', max_length=200)
    conteudo = RichTextField('Conteúdo', config_name='juniorlima')

    imagem = ThumbnailerImageField(upload_to='imagens', blank=True)

    categoria = models.ForeignKey(Categoria)
    slug = models.SlugField(max_length=110, unique=True, blank=True, null=True)
    cliques = models.IntegerField('Cliques', default=0, editable=False)
    data_publicacao = models.DateTimeField('Data de publicação', auto_now_add=True)
    data_atualizacao = models.DateTimeField('Data de publicação', auto_now=True)
    usuario = models.ForeignKey(User, related_name='usuario_add', blank=True, null=True)
    usuario_modificou = models.ForeignKey(User, related_name='usuario_mod', blank=True, null=True)
    def __unicode__(self):
        return self.titulo
    @models.permalink
    def get_absolute_url(self):
        return ('post-detail', (), {'slug': self.slug})
        # http://stackoverflow.com/questions/14170473/get-absolute-url-in-django-when-using-class-based-views
    def save(self, force_insert=False, force_update=False):
        super(Postagem, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
            pass
    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'

# SIGNALS
def postagem_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)

signals.pre_save.connect(postagem_pre_save, sender=Postagem)

def categoria_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(categoria_pre_save, sender=Categoria)