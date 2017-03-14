# -*- coding: utf-8 -*-
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
from igenius.thumbs import ImageWithThumbsField
from cliente.models import *

PUBLICIDADE_CHOICES = (('1', 'Bloco Esquerda'),('2', 'Banner Extra'),('3', 'Interna Bloco'),('4', 'Adsense Aranha Ceu'),('5', 'Adsense Banner Extra'),('6', 'Adsense Desktop'),('7', 'Adsense Mobile'),('8', 'Adsense Footer Noticia'))

class Publicidade(models.Model):
    ativo = models.BooleanField('Status',default=True)
    nome=models.CharField("Nome",max_length=100)
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente',blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    valorEntrada = models.FloatField(blank=True, null=True)
    valorFinal = models.FloatField(blank=True, null=True)
    arquivo = models.FileField(upload_to='Publicidade', blank=True, null=True)
    data_entrada=models.DateTimeField("Data de entrada",default=datetime.now)
    data_saida=models.DateTimeField("Data de saída")
    tipo=models.CharField('Tipo da publicidade', max_length=2, choices = PUBLICIDADE_CHOICES)
    url=models.URLField("Site da publicidade", blank=True, null=True)
    patrocinado = models.BooleanField(default=False, blank=True)
    slugpublicidade = models.SlugField(max_length=200)
    adsense = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('igenius.views.patrocinado', kwargs={'slugpublicidade': self.slugpublicidade})

    class Meta:
        verbose_name_plural = "Inserir Publicidades"

    def __unicode__(self):
        return self.nome

    def Final(self):
        r = self.valor - self.valorEntrada
        self.valorFinal = r
        return r



# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

def publicidade_pre_save(signal, instance, sender, **kwargs):
    instance.slugpublicidade = slugify(instance.nome)
signals.pre_save.connect(publicidade_pre_save, sender=Publicidade)