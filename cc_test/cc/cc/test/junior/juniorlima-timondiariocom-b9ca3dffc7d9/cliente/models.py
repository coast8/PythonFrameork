# coding=utf-8
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from igenius.models import Bairros


class Cliente(models.Model):
    #Dadosdo Anunciante
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True, null=True)

    #Dados Pessoais
    rg = models.CharField('RG/Inscrição Estadual',max_length=100, blank=True, null=True)
    cpfcnpj = models.CharField('CPF/CNPJ', max_length=100, blank=True, null=True)
    endereco = models.CharField('Endereço',max_length=100, blank=True, null=True)
    bairro = models.ForeignKey(Bairros, verbose_name='Bairro')

    telefone = models.CharField('Telefone',max_length=20)
    celular = models.CharField('Celular',max_length=20, blank=True, null=True)
    email = models.EmailField('Email',blank=True, null=True)
    foto = models.ImageField('Foto',upload_to='fotos',blank=True, null=True)

    slugcliente = models.SlugField(max_length=200,blank=True, null=True)

    class Meta:
        verbose_name_plural = "Cadastrar Cliente"

    def __unicode__(self):
        return self.nome


# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

def cliente_pre_save(signal, instance, sender, **kwargs):
    instance.slugcliente = slugify(instance.nome)
signals.pre_save.connect(cliente_pre_save, sender=Cliente)