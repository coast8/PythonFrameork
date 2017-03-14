# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

import datetime
now = datetime.datetime.now()


from django.db import models
from django.contrib.sitemaps import ping_google
from django.core.urlresolvers import reverse
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from easy_thumbnails.fields import ThumbnailerImageField
from ckeditor.fields import RichTextField

from core.choices import BLOG_POSTAGEM_POSICAO, COLOR_CSS_CHOICES

# Categoria de notícias
class Categoria(models.Model):
    publicar = models.BooleanField(default=True)
    nome = models.CharField(max_length=30)
    descricao = models.TextField(blank=True, null=True)
    menu = models.BooleanField(default=False)
    color = models.CharField('Atributo de cor',blank=True, null=True, max_length=20, choices=COLOR_CSS_CHOICES)
    cliques = models.IntegerField('Cliques', default=0, editable=False)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    class Meta:
        verbose_name_plural = 'Categoria de notícias'
    def __unicode__(self):
        return self.nome
    def get_absolute_url(self):
        return reverse('portal.views.categoria', kwargs={'slug': self.slug})

class Noticia(models.Model):
    publicar = models.BooleanField('Publicar', default=True)
    destaque = models.BooleanField('Destaque', default=True)
    titulo = models.CharField('Título', max_length=100, unique=True)
    subtitulo = models.CharField('Subtítulo', max_length=200)
    conteudo = RichTextField('Conteúdo', config_name='default')

    posicao_foto = models.CharField('Posição da foto', max_length=2, choices=BLOG_POSTAGEM_POSICAO, default='1')
    slug = models.SlugField(max_length=110, unique=True, blank=True, null=True)
    cliques = models.IntegerField('Cliques', default=0, editable=False)
    data_publicacao = models.DateTimeField('Data de publicação', default=now)
    data_atualizacao = models.DateTimeField('Data de publicação', auto_now=True)
    usuario = models.ForeignKey(User, related_name='usuario_add', blank=True, null=True)
    usuario_modificou = models.ForeignKey(User, related_name='usuario_mod', blank=True, null=True)
    def __unicode__(self):
        return self.titulo
    def get_absolute_url(self):
        return reverse('portal.views.noticia', kwargs={'slug': self.slug})



class Postagem(Noticia):
    chamada = models.CharField('Chamada', max_length=20, blank=True, null=True)
    imagem = ThumbnailerImageField(upload_to='imagens', blank=True)
    categoria = models.ForeignKey(Categoria)
    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
    def save(self, force_insert=False, force_update=False):
        super(Postagem, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
            pass
    # Next and preview
    def get_next(self):
        next = Postagem.objects.filter(id__gt=self.id)
        if next:
            return next[0]
        return ''

    def get_prev(self):
        prev = Postagem.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev[0]
        return ''

class VideoPostagem(models.Model):
    url = models.CharField('Link do YouTube', max_length=15, help_text='Insira o código depois do igual do link do YouTube. Ex: "bTYOWVnyISc"')
    postagem = models.ForeignKey(Postagem, related_name='video_set')
    comentario = models.CharField('Comentário', max_length=200, blank=True, null=True)
    class Meta:
        verbose_name = 'Adicionar vídeo'
        verbose_name_plural = 'Adicionar vídeo'


# SIGNALS
def postagem_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)

signals.pre_save.connect(postagem_pre_save, sender=Postagem)

def categoria_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(categoria_pre_save, sender=Categoria)