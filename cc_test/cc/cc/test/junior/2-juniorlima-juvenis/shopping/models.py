# -*- coding: utf-8 -*-

__author__ = 'Junior Lima'

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from core.choices import SHOPPING_SITUACAO_PRODUTO, SHOPPING_STATUS_CHOICES
from core.models import BaseNoticiaAbstract
from core.thumbs import ImageWithThumbsField

from administrativo.models import Empresa

def content_image_name(instance, filename):
    return '/'.join(['arquivos/compras', str(instance.nomecategoria.slugcatproduto), filename])

class CategoriaProduto(models.Model):
    publicar = models.BooleanField(default=True)
    nome = models.CharField(max_length=30, unique=True)
    slugcatproduto = models.SlugField(max_length=100, blank=True, unique=True)
    descricao = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    def __unicode__(self):
        return self.nome
    def get_absolute_url(self):
        return reverse('noticias.views.produtocategoria', kwargs={'slugcatproduto': self.slugcatproduto})

class Marca(models.Model):
    publicar = models.BooleanField(default=True)
    nome = models.CharField('Marca', max_length=30)
    def __unicode__(self):
        return self.nome

class Produto(BaseNoticiaAbstract):
    categoria_nome = models.ForeignKey(CategoriaProduto, verbose_name='Categoria')
    marca_nome = models.ForeignKey(Marca, verbose_name='Marca')
    loja_nome = models.ForeignKey(Empresa, verbose_name='Loja')
    status_ch = models.CharField('Status', max_length=2, choices=SHOPPING_STATUS_CHOICES, default='1')
    situacao_ch = models.CharField('Situação', max_length=2, choices=SHOPPING_SITUACAO_PRODUTO, default='1')
    fotoum = ImageWithThumbsField('Foto Principal', upload_to='pasta', sizes=((300,225),(800,600),(1200,1024)))
    fotodois = ImageWithThumbsField('Foto Principal', blank=True, null=True, upload_to='pasta', sizes=((300,225),(640,480)))
    fototres = ImageWithThumbsField('Foto Principal', blank=True, null=True, upload_to='pasta', sizes=((300,225),(640,480)))
    googlemaps = models.TextField(blank=True, null=True)
    preconormal = models.CharField(max_length=6, help_text='Valor separado por ponto. 32.00')
    desconto = models.CharField(max_length=6, help_text='Valor separado por ponto. 2.00')
    precofinal = models.CharField(max_length=6, help_text='Valor separado por ponto. 30.00')
    dataentrada = models.DateField(auto_now_add=True)
    datasaida = models.DateField(auto_now_add=True)
    
    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('noticias.views.produto', kwargs={'slugcategoria': self.categoria_nome.slugcatproduto,
                                                         'slugproduto': self.slug
        })

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

def categoria_pre_save(signal, instance, sender, **kwargs):
    instance.slugcatproduto = slugify(instance.nome)
signals.pre_save.connect(categoria_pre_save, sender=CategoriaProduto)

def produto_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        slug = slugify(instance.titulo)
        novaslug = slug
        contador = 0

        while  Produto.objects.filter(slug = novaslug).exclude(id=instance.id).count() > 0:
            contador += 1
            novaslug = '%s-%d'%(slug, contador)
        instance.slug = novaslug
signals.pre_save.connect(produto_pre_save, sender=Produto)