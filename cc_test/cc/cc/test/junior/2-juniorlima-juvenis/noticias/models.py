# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError

from lib.tagging.models import Tag
from lib.tagging_autocomplete.models import TagAutocompleteField
from core.thumbs import ImageWithThumbsField

from core.models import Noticia
from core.choices import NOTICIAS_CATEGORIA_EVENTO
from core.destino_imagem import noticia_noticia, noticia_album

from locais.models import LocalEvento, Cidade


# Categoria de notícias
class Categoria(models.Model):
    publicar = models.BooleanField(default=True)
    nome = models.CharField(max_length=30)
    descricao = models.TextField(blank=True, null=True)
    cliques = models.IntegerField('Cliques', default=0, editable=False)
    slugcategoria = models.SlugField(max_length=100, blank=True, unique=True)
    class Meta:
        verbose_name_plural = 'Categoria de notícias'
    def __unicode__(self):
        return self.nome
    def get_absolute_url(self):
        return reverse('noticias.views.categorianoticia', kwargs={'slugcategoria': self.slugcategoria})



class Noticias(Noticia):
    subtitulo = models.CharField(max_length=200)
    fonte = models.CharField(max_length=30, blank=True, null=True)
    chamada = models.CharField(max_length=30)
    categoria_nome = models.ForeignKey(Categoria, verbose_name='Categoria')
    imagem = ImageWithThumbsField('Imagem Destaque', upload_to=noticia_noticia, sizes=((800,600),(200,150)))
    tags = TagAutocompleteField()
    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
    def __unicode__(self):
        return self.titulo
    def save(self, *args, **kwargs):
        try:
            this = Noticias.objects.get(id=self.id)
            if this.imagem != self.imagem:
                this.imagem.delete(save=False)
        except: pass # when new photo then we do nothing, normal case
        super(Noticias, self).save(*args, **kwargs)
        if not self.slug:
            if self.categoria_nome_id == 6: # Notícias
                self.slug = '%i-%s' % (self.id, slugify(self.titulo))
            else:
                self.slug = '%s' % slugify(self.titulo)
        super(Noticias, self).save()
    def get_absolute_url(self):
        if self.categoria_nome_id == 3:
            for item in self.evento_noticia_set.all():
                estado = (slugify(item.cidade.uf.sigla))
                cidade = (slugify(item.cidade.slugcidade))
                return reverse('noticias.views.evento', kwargs={'slugcategoria':self.categoria_nome.slugcategoria,
                                                                'slugestado': estado,
                                                                'slugcidade': cidade,
                                                                 'slug': self.slug})
        else:
            return reverse('noticias.views.noticia', kwargs={'slugcategoria':self.categoria_nome.slugcategoria,
                                                         'slug': self.slug
        })
    def get_tags(self):
        return Tag.objects.get_for_object(self)

class Eventos(models.Model):
    evento_noticia = models.ForeignKey(Noticias, related_name='evento_noticia_set')
    dataevento = models.DateField('Data do evento', blank=True, null=True)
    categoria = models.CharField('Categoria', max_length=2, choices=NOTICIAS_CATEGORIA_EVENTO, default=1)
    ingressos = models.CharField('Preço do ingresso', max_length=10, blank=True, null=True)
    organizacao = models.CharField('Organização', max_length=40)
    cidade = models.ForeignKey(Cidade, blank=True, null=True)
    local = models.ForeignKey(LocalEvento, blank=True, null=True)
    class Meta:
        order_with_respect_to = '-dataevento'
        unique_together = (('codigo', 'dataevento'),)
    def __unicode__(self):
        if self.local:
            return '%s - %s' % (self.evento_noticia.titulo, self.local.cidade_uf.uf)
        else:
            return '%s - %s' % (self.evento_noticia.titulo, self.organizacao)
    def evento_cidade(self):
        return  self.cidade.nome
    evento_cidade.short_description = 'Cidade'
    def evento_estado(self):
        return  self.cidade.uf.nome
    evento_estado.short_description = 'Estado'
    def get_absolute_url(self):
        return reverse('noticias.views.evento', kwargs={'slugcategoria':self.evento_noticia.categoria_nome.slugcategoria,
                                                        'slugestado': slugify(self.cidade.uf.sigla),
                                                        'slugcidade': self.cidade.slugcidade,
                                                        'slug': self.evento_noticia.slug,
        })

    def clean(self):
        if not self.id:
            if self.cidade is None and self.local is None:
                raise ValidationError('Preencha a cidade ou local do evento.')
            if self.cidade is not None and self.local is not None:
                raise ValidationError('Favor deixar o campo cidade em branco')
    def save(self):
        super(Eventos, self).save()
        self.evento_noticia.slug = '%s' % slugify(self.evento_noticia_id)
        self.evento_noticia.categoria_nome_id = 5
        if self.cidade is None:
            self.cidade_id = self.local.cidade_uf_id
        super(Eventos, self).save()
    class Meta:
        verbose_name = 'Notícias - Evento'
        verbose_name_plural = 'Notícias - Eventos'

class VideoNoticia(models.Model):
    usarvideo = models.BooleanField(default=False)
    url = models.CharField(max_length=15, help_text="fhbTBA64FkU")
    video_noticia = models.ForeignKey(Noticias, related_name='video_noticia_set')
    def __unicode__(self):
        return '%s - %s' % (self.video_noticia.titulo, self.url)
    def save(self):
        if self.url is not None:
            self.usarvideo = 1
        super(VideoNoticia, self).save()
    class Meta:
        verbose_name_plural = 'Adicionar vídeo do YouTube a notícia'

class Album(Noticia):
    cantor_nome = models.ForeignKey('letras.Cantor', verbose_name='Cantor')
    ano = models.PositiveSmallIntegerField(max_length=4, default=2014)
    imagem = ImageWithThumbsField('Imagem Destaque', upload_to=noticia_album, sizes=((300,225),(100,75)), blank=True, null=True)
    def __unicode__(self):
        return "%s - %s" % (self.cantor_nome.nome, self.titulo)
    def cantor_album(self):
        return self.cantor_nome.nome
    def get_absolute_url(self):
        return reverse('noticias.views.download', kwargs={'slugcantor':self.cantor_nome.slugcantor,
                                                          'slugalbum': self.slug,
        })

    def download_url(self):
        return reverse('noticias.views.downloadlink', kwargs={'cantor_id': self.cantor_nome_id,
                                                          'download_id': self.id})
    class Meta:
        verbose_name = 'Download'
        verbose_name_plural = 'Downloads'
        #unique_together = (("cantor_nome", "titulo"),)
        ordering = ['-criado_em']

class Link(models.Model):
    link = models.URLField(max_length=30)
    link_downloadalbum = models.ForeignKey(Album, verbose_name='Álbum')
    def get_absolute_url(self):
        return reverse('noticias.views.download', kwargs={'cantor_id': self.link_downloadalbum.cantor_nome_id,
                                                          'download_id':self.id,
                                                          })
    def __unicode__(self):
        return "%s - %s - %s" % (self.link_downloadalbum.cantor_nome, self.link_downloadalbum.titulo, self.link)
    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'



# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify


def categoria_pre_save(signal, instance, sender, **kwargs):
    instance.slugcategoria = slugify(instance.nome)

signals.pre_save.connect(categoria_pre_save, sender=Categoria)

def album_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.titulo)

signals.pre_save.connect(album_pre_save, sender=Album)