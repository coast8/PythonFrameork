# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.localflavor.br.br_states import STATE_CHOICES
from django.contrib.auth.models import User

from core.destino_imagem import local_local
from core.thumbs import ImageWithThumbsField

from lib.ckeditor.fields import RichTextField

class Estado(models.Model):
    sigla = models.CharField('Sigla', max_length=2, unique=True)
    nome = models.CharField('Estado', max_length=20, unique=True)
    def __unicode__(self):
        return '%s - %s' % (self.sigla, self.nome)

class Cidade(models.Model):
    nome = models.CharField('Cidade', max_length=50)
    uf = models.ForeignKey(Estado)
    slugcidade = models.SlugField(max_length=100, blank=True, unique=True)
    def __unicode__(self):
        return '%s %s' % (self.nome, self.uf)
    def evento_estado(self):
        estado = (slugify(self.uf.sigla))
        return reverse('noticias.views.evento_estado', kwargs={'slugestado': estado})
    def evento_cidade(self):
        estado = (slugify(self.uf.sigla))
        return reverse('noticias.views.evento_cidade', kwargs={'slugestado':estado,
                                                               'slugcidade': self.slugcidade,})
    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        unique_together = (("nome", "uf"),)

class CategoriaLocal(models.Model):
    nome = models.CharField('Nome', max_length=100, unique=True)
    slugcategoria = models.SlugField(max_length=100, blank=True, unique=True)
    def __unicode__(self):
        return  self.nome
    def get_absolute_url(self):
        return reverse('noticia.views.localcategoria', kwargs={'slugcategoria': self.slugcategoria})
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class LogradourosLocal(models.Model):
    endereco = models.CharField('Endereço', max_length=64, unique=True)
    cep = models.CharField('CEP', max_length=9, blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=30, blank=True, null=True)
    cidade_uf = models.ForeignKey(Cidade, verbose_name='Cidade Estado')
    telefone = models.CharField('Telefone', max_length=14, blank=True, null=True)
    def __unicode__(self):
        return '%s - %s' % (self.endereco, self.local_nome.nome)
    class Meta:
        verbose_name = 'Informações sobre local'
        verbose_name_plural = 'Informações sobre locais'

class Local(LogradourosLocal):
    publicar = models.BooleanField(default=True)
    destaque = models.BooleanField(default=False)
    nome = models.CharField('Nome', max_length=100)
    categoria_nome = models.ForeignKey(CategoriaLocal)
    imagem = ImageWithThumbsField('Imagem do local', upload_to=local_local, sizes=((800,600),(300,225)), blank=True, null=True)
    site = models.URLField('Site', max_length=100, blank=True, null=True)
    conteudo = RichTextField('Conteúdo', config_name='juniorlima', blank=True, null=True)

    lat_long = models.CharField('Latidute e longitude', max_length=30, blank=True, null=True, help_text='-5.110522,-42.76527')
    sluglocal = models.SlugField(max_length=100, blank=True, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    cliques = models.IntegerField('Cliques', default=0, editable=False)

    usuario = models.ForeignKey(User, related_name='user_add_%(class)ss', blank=True, null=True)
    usuario_modificou = models.ForeignKey(User, related_name='user_mod_%(class)ss', blank=True, null=True)
    def get_absolute_url(self):
        return reverse('noticias.views.local', kwargs={'slugcidade': self.cidade_uf.slugcidade,
                                                       'slugdolocal':self.sluglocal})
    def __unicode__(self):
        return  self.nome
    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locais'

class LocalEvento(Local):
    def save(self):
        super(LocalEvento, self).save()
        self.sluglocal = '%s' % slugify(self.nome)
        super(LocalEvento, self).save()
    class Meta:
        verbose_name = 'Local de Evento'
        verbose_name_plural = 'Locais de Evento'

from django.db.models import signals
from django.template.defaultfilters import slugify

def categoria_local_pre_save(signal, instance, sender, **kwargs):
    instance.slugcategoria = slugify(instance.nome)
signals.pre_save.connect(categoria_local_pre_save, sender=CategoriaLocal)

def local_pre_save(signal, instance, sender, **kwargs):
    instance.sluglocal = slugify(instance.nome)
signals.pre_save.connect(local_pre_save, sender=Local)

def cidade_pre_save(signal, instance, sender, **kwargs):
    instance.slugcidade = slugify(instance.nome)
signals.pre_save.connect(cidade_pre_save, sender=Cidade)