# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.sitemaps import ping_google
from django.db.models import signals
from django.template.defaultfilters import slugify
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
    conteudo = RichTextField('Conteúdo', config_name='juniorlima')

    #posicao_foto = models.CharField('Posição da foto', max_length=2, choices=BLOG_POSTAGEM_POSICAO, default='1')
    imagem = ThumbnailerImageField(upload_to='imagens', blank=True)

    categoria = models.ForeignKey(Categoria)
    slug = models.SlugField(max_length=110, unique=True, blank=True, null=True)
    cliques = models.IntegerField('Cliques', default=0, editable=False)
    data_publicacao = models.DateTimeField('Data de publicação', default=datetime.datetime.now())
    data_atualizacao = models.DateTimeField('Data de publicação', auto_now=True)
    usuario = models.ForeignKey(User, related_name='usuario_add', blank=True, null=True)
    usuario_modificou = models.ForeignKey(User, related_name='usuario_mod', blank=True, null=True)
    def __unicode__(self):
        return self.titulo
    def get_absolute_url(self):
        return reverse('assessoria.views.noticia', kwargs={'slug': self.slug})
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

class VideoPostagem(models.Model):
    url = models.CharField('Link do YouTube', max_length=15, help_text='Insira somente o código depois do igual. Ex: "bTYOWVnyISc"')
    postagem = models.ForeignKey(Postagem, related_name='video_set')
    comentario = models.CharField('Comentário', max_length=200, blank=True, null=True)
    class Meta:
        verbose_name = 'Adicionar vídeo'
        verbose_name_plural = 'Adicionar vídeo'

class Institucional(models.Model):
    perfil = RichTextField('Perfil')


class Evento(models.Model):
    data_evento = models.DateTimeField('Data do evento')
    postagem = models.ForeignKey(Postagem, related_name='evento_post')
    def __unicode__(self):
        #return self.postagem.titulo
        return self.data_evento.strftime("%d %m %Y ")
    def save(self, *args, **kwargs):
        self.categoria_id= 1
        super(Evento, self).save(*args, **kwargs)

class Frase(models.Model):
    publicar = models.BooleanField('Publicar', default=True)
    frase = models.CharField('Frase', max_length=160)
    data_publicacao = models.DateTimeField('Data de publicação', auto_now_add=True)
    data_atualizacao = models.DateTimeField('Data de publicação', auto_now=True)
    usuario = models.ForeignKey(User, related_name='usuario_add_frase', blank=True, null=True)
    usuario_modificou = models.ForeignKey(User, related_name='usuario_mod_frase', blank=True, null=True)
    class Meta:
        verbose_name = 'Frase do Dr Pessoa'
        verbose_name_plural = 'Frases do Dr Pessoa'
    def __unicode__(self):
        return self.frase


def postagem_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)

signals.pre_save.connect(postagem_pre_save, sender=Postagem)

def categoria_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(categoria_pre_save, sender=Categoria)
