# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from core.thumbs import ImageWithThumbsField
from core.choices import CAMPEONATO_JOGADOR_C, CAMPEONATO_QUADRA_C, CAMPEONATO_TURNO_C
from core.destino_imagem import campeonato_jogador

class Campeonato(models.Model):
    "Representa um nomeCampeonato"
    nome = models.CharField('Nome', max_length=30)
    ano = models.CharField('Ano', max_length=4)
    slugcampeonato = models.SlugField(max_length=255, blank=True, unique=True)
    def __unicode__(self):
        return "%s - %s" % (self.nome, self.ano)
    def get_absolute_url(self):
        return reverse('noticias.views.campeonato', kwargs={'slugcampeonato': self.slugcampeonato})
    class Meta:
        verbose_name_plural = 'campeonato'
        verbose_name = 'campeonato'

class Time(models.Model):
    "Representa um clube"
    nome = models.CharField('Nome do Time', max_length=50, unique=True)
    campeonato_nome = models.ForeignKey(Campeonato, verbose_name='campeonato')
    bairro = models.CharField('Bairro', max_length=30)
    igreja = models.CharField('Igreja', max_length=30)
    #Perguntas
    jogadorfora = models.CharField('E se pudesse jogador de fora', blank=True, null=True, max_length=100, choices=CAMPEONATO_JOGADOR_C)
    quadra = models.CharField('Quadra de sua preferência', blank=True, null=True, max_length=100, choices=CAMPEONATO_QUADRA_C)
    turno = models.CharField('Jogaria a noite?', blank=True, null=True, max_length=100, choices=CAMPEONATO_TURNO_C)
    #Responsável
    responsavel = models.CharField('Responsável', max_length=30)
    telefoneresponsavel = models.CharField('Telefone', max_length=12)
    emailresponsavel = models.EmailField('Email', max_length=50)
    facebookresponsavel = models.URLField('Facebook', max_length=100, blank=True, null=True)
    #Tecnico
    tecnico = models.CharField('Nome', max_length=30, blank=True, null=True)
    telefonetecnico = models.CharField('Telefone', max_length=12, blank=True, null=True)
    #Outros
    slugtime = models.SlugField(max_length=255, blank=True, unique=True)
    cliques = models.IntegerField('Cliques', default=0, editable=False)
    usuario = models.ForeignKey(User, related_name='user_add_time', blank=True, null=True)
    usuario_modificou = models.ForeignKey(User, related_name='user_mod_time', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.nome
    def get_absolute_url(self):
        return reverse('noticias.views.time', kwargs={'slugcampeonato': self.campeonato_nome.slugcampeonato,
                                                      'slugtime': self.slugtime
        })

class Jogador(models.Model):
    "Representa um jogador"
    escalado = models.BooleanField('Escalado', default=True)
    nome = models.CharField('Nome', max_length=30)

    datanascimento = models.DateField('Data de Nascimento', blank=True, null=True)
    rg = models.CharField('RG', max_length=10, blank=True, null=True)

    numero = models.SmallIntegerField('Número do Jogador', blank=True, null=True)
    telefone = models.CharField('Telefone', max_length=12, unique=True)
    facebook = models.URLField('Facebook', max_length=100, blank=True, null=True)
    foto = ImageWithThumbsField('Foto', blank=True, null=True, upload_to=campeonato_jogador, sizes=((800,600),(120,90),(400,300)))
    time_nome = models.ForeignKey(Time, verbose_name='Time')

    slugjogador = models.SlugField(max_length=255, blank=True, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    cliques = models.IntegerField('Cliques', default=0, editable=False)
    usuario = models.ForeignKey(User, related_name='user_add_jogador', blank=True, null=True)
    usuario_modificou = models.ForeignKey(User, related_name='user_mod_jogador', blank=True, null=True)
    url = models.CharField(max_length=15, help_text="fhbTBA64FkU")
    def __unicode__(self):
        return self.nome
    class Meta:
        verbose_name_plural = 'Jogadores'
        verbose_name = 'Jogadores'
    def get_absolute_url(self):
        return reverse('noticias.views.jogador', kwargs={'slugcampeonato': self.time_nome.campeonato_nome.slugcampeonato,
                                                         'slugtime': self.time_nome.slugtime,
                                                         'slugjogador': self.slugjogador
        })

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

def campeonato_pre_save(signal, instance, sender, **kwargs):
    instance.slugcampeonato = slugify(instance.nome)

signals.pre_save.connect(campeonato_pre_save, sender=Campeonato)

def time_pre_save(signal, instance, sender, **kwargs):
    instance.slugtime = slugify(instance.nome)

signals.pre_save.connect(time_pre_save, sender=Time)