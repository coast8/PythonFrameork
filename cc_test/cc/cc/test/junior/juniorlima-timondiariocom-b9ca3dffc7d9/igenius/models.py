# -*- coding: utf-8 -*-
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
from igenius.thumbs import ImageWithThumbsField
from lib.ckeditor.fields import RichTextField
from lib.tagging_autocomplete.models import TagAutocompleteField

SISTEMA_CHOICES = (('1','Windows'),('2','Linux'),('3','iOS'),('4','MacOS'))
UNI_CHOICES = (('1','Kb'),('2','MB'),('3','GB'),('4','TB'))
SEXO_CHOICES = (('1','Masculino'),('2','Feminino'))
TIPO_CHOICES = (('1','Pessoa Física'),('2','Pessoa Jurídica'))

def content_image_name(instance, filename):
    return '/'.join(['programas/icones', str(instance.nomecategoria.slugcategoria),str(instance.subcategoria.slugsubcategoria),filename])
def content_programa_arquivo(instance, filename):
    return '/'.join(['programas/arquivo', str(instance.nomecategoria.slugcategoria),str(instance.subcategoria.slugsubcategoria),str(instance.slug),filename])
def content_games_arquivo(instance, filename):
    return '/'.join(['games/arquivo', str(instance.nomecategoria.slugcategoria),str(instance.subcategoria.slugsubcategoria),filename])
def imagem_galeria(instance, filename):
    return '/'.join(['programas/icones', str(instance.nomePrograma.nomecategoria.slugcategoria),str(instance.nomePrograma.subcategoria.slugsubcategoria),str(instance.nomePrograma.slug),filename])
def imagem_galeria_all(instance, filename):
    return '/'.join(['arquivos/galeria', filename])
def content_image_name_noticia(instance, filename):
    return '/'.join(['noticias', str(instance.categoria.slugcategoria),filename])
def content_image_name_tutorial(instance, filename):
    return '/'.join(['tutoriais', str(instance.nomecategoria.slugcategoria),filename])
def content_image_name_review(instance, filename):
    return '/'.join(['reviews',filename])

class uf(models.Model):
    nome = models.CharField(max_length=2)
    estado = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    sluguf = models.SlugField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Cadastrar UF"

    def __unicode__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.ForeignKey(uf, blank=True, null=True)
    cep = models.TextField(max_length=15, blank=True, null=True)
    prefeitura = models.CharField('Endereço Prefeitura', max_length=100, blank=True, null=True)
    prefeito = models.CharField('Atual Prefeito',max_length=100, blank=True, null=True)
    contato = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    site = models.URLField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    slugcidade = models.SlugField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Cadastrar Cidade"

    def __unicode__(self):
        return self.nome

class Bairros(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade)
    endassociacao = models.CharField(max_length=200,blank=True, null=True)
    contato = models.CharField(max_length=100,blank=True, null=True)
    slugbairro = models.SlugField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Cadastrar Bairro"

    def __unicode__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('igenius.views.bairro', kwargs={'sluguf': self.cidade.uf.sluguf,'slugcidade': self.cidade.slugcidade,'slugbairro': self.slugbairro})


class Fonte(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    site = models.URLField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Cadastrar Fonte"

    def __unicode__(self):
        return self.nome

class Colaborador(models.Model):
    publicar=models.BooleanField(default=True)
    usuario = models.ForeignKey(User,verbose_name='Usuário')
    nome=models.CharField(max_length=50)
    cargo=models.CharField(max_length=50, blank=True, null=True)
    email=models.EmailField()
    telefone=models.CharField('WattsApp',max_length=12,help_text='XX-XXXX-XXXX', blank=True, null=True)
    thumbs=models.ImageField(upload_to='thumb',help_text='85px-85px', blank=True, null=True)
    descricao=models.TextField(blank=True, null=True)
    orkut=models.URLField("Orkut", blank=True, null=True)
    twitter=models.URLField("Twitter", blank=True, null=True)
    facebook=models.CharField(max_length=200, blank=True, null=True)
    linkedin=models.URLField("LinkedIn", blank=True, null=True)
    google=models.CharField(max_length='200',blank=True,null=True)
    data = models.DateTimeField('Data de publicação',default=datetime.now)

    class Meta:
        verbose_name_plural = "Cadastrar Colaboradores"
    def __unicode__(self):
        return self.nome

class CategoriaNoticia(models.Model):
    nome = models.CharField(max_length=100,unique=True)
    slugcategoria = models.SlugField(max_length=100, blank=True, unique=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Cadastrar Categoria(Notícia)"
    def __unicode__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('igenius.views.categoria', kwargs={'slugcategoria': self.slugcategoria})


class SubCategoria(models.Model):
    nome = models.CharField(max_length=100,unique=True)
    categoria = models.ForeignKey(CategoriaNoticia, verbose_name='Categoria')
    descricao = models.TextField(blank=True,null=True)
    slugsubcategoria = models.SlugField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Cadastrar Sub Categoria(Notícia)"
    def __unicode__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('igenius.views.subcategoria', kwargs={'slugcategoria': self.categoria.slugcategoria,'slugsubcategoria': self.slugsubcategoria})


class Posicao(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    data = models.DateTimeField('Data de publicação',default=datetime.now,blank=True)

    class Meta:
        verbose_name_plural = "Cadastrar Posição"
    def __unicode__(self):
        return self.nome

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

def categoriaNoticia_pre_save(signal, instance, sender, **kwargs):
    instance.slugcategoria = slugify(instance.nome)
signals.pre_save.connect(categoriaNoticia_pre_save, sender=CategoriaNoticia)

def uf_pre_save(signal, instance, sender, **kwargs):
    instance.sluguf = slugify(instance.nome)
signals.pre_save.connect(uf_pre_save, sender=uf)

def cidade_pre_save(signal, instance, sender, **kwargs):
    instance.slugcidade = slugify(instance.nome)
signals.pre_save.connect(cidade_pre_save, sender=Cidade)

def bairro_pre_save(signal, instance, sender, **kwargs):
    instance.slugbairro = slugify(instance.nome)
signals.pre_save.connect(bairro_pre_save, sender=Bairros)

def subcategoriaNoticia_pre_save(signal, instance, sender, **kwargs):
    instance.slugsubcategoria = slugify(instance.nome)
signals.pre_save.connect(subcategoriaNoticia_pre_save, sender=SubCategoria)