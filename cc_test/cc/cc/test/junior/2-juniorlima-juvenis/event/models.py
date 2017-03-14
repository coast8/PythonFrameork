# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class LocalEvento(models.Model):
    nome = models.CharField('Nome do local', max_length=50)
    endereco = models.CharField('Endereço', max_length=100)
    bairro = models.CharField('Bairro', max_length=50, blank=True, null=True)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=30)
    class Meta:
        verbose_name = 'Local do Evento'
        verbose_name_plural = 'Local do Evento'
    def __unicode__(self):
        return self.nome

class Evento(models.Model):
    publicar = models.BooleanField('Publicar')
    nome = models.CharField('Nome', max_length=100, unique=True)
    data_evento = models.DateField('Data do evento')

    chamada = models.CharField('Chamada', max_length=100)
    descricao = models.TextField('Descrição do evento')

    telefone = models.CharField('Telefone', max_length=14)
    email = models.EmailField('Email', max_length=100, blank=True, null=True)

    facebook = models.URLField('Facebook', max_length=21, blank=True, null=True)
    twitter = models.URLField('Twitter', max_length=21, blank=True, null=True)
    plus = models.URLField('Plus', max_length=21, blank=True, null=True)
    youtube = models.URLField('Youtube', max_length=21, blank=True, null=True)
    instagram = models.URLField('Instagram', max_length=21, blank=True, null=True)
    pinterest = models.URLField('Pinterest', max_length=21, blank=True, null=True)
    linkedid = models.URLField('Linked ID', max_length=21, blank=True, null=True)

    #local = models.ForeignKey(LocalEvento)

    slugevento = models.SlugField(max_length=100, blank=True, null=True, unique=True)
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
    def __unicode__(self):
        return self.nome
    def get_absolute_url(self):
        return reverse('event.views.evento', kwargs={'slugevento': self.slugevento})

class Ingresso(models.Model):
    publicar = models.BooleanField('Publicar')
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField(max_digits=5 ,decimal_places=2)
    evento = models.ForeignKey(Evento)
    class Meta:
        verbose_name = 'Ingresso'
        verbose_name_plural = 'Ingressos'
    def __unicode__(self):
        return '%s - %s' % (self.nome, self.preco)

class Pessoa(models.Model):
    publicar = models.BooleanField('Publicar', default=True)
    nome = models.CharField('Nome', max_length=100)
    apelido = models.CharField('Apelido', max_length=30, blank=True, null=True)
    telefone = models.CharField('Telefone', max_length=14)
    email = models.EmailField('Email', max_length=100, blank=True, null=True)
    foto = models.ImageField('Foto', upload_to='foto')

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
    def __unicode__(self):
        return self.nome

class Organizacao(Pessoa):
    evento = models.ForeignKey(Evento)
    user = models.OneToOneField(User)
    class Meta:
        verbose_name = 'Organização'
        verbose_name_plural = 'Organização'
    def __unicode__(self):
        return self.nome

class Participante(Pessoa):
    evento = models.ForeignKey(Evento)
    class Meta:
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'
    def __unicode__(self):
        return self.nome


class TipoEvento(models.Model):
    nome = models.CharField('Nome', max_length=50, unique=True)
    class Meta:
        verbose_name = 'Tipo de evento'
        verbose_name_plural = 'Tipo de evento'
    def __unicode__(self):
        return self.nome

class Ministrante(models.Model):
    publicar = models.BooleanField('Publicar')
    nome = models.CharField('Nome', max_length=50)
    origem = models.CharField('De onde é', max_length=70)
    foto = models.ImageField('Imagem', blank=True, null=True, upload_to='ministrante')
    ficha_tecnica = models.TextField('Ficha técnica')
    tipo_evento = models.ForeignKey(TipoEvento)
    evento = models.ForeignKey(Evento)
    class Meta:
        verbose_name = 'Ministrante'
        verbose_name_plural = 'Ministrantes'
    def __unicode__(self):
        return self.nome

class DiasdePalestra(models.Model):
    data = models.DateField('Data da palestra')
    evento = models.ForeignKey(Evento, related_name='dia_set')
    class Meta:
        verbose_name = 'Dia de palestra'
        verbose_name_plural = 'Dias de palestra'
    def __unicode__(self):
        return str(self.data)

class Programacao(models.Model):
    programa = models.CharField('Nome da palestra ou show', max_length=200)
    descricao = models.TextField('Descrição')
    hor_prog = models.TimeField('Horário da programação')
    dia_prog = models.DateTimeField('Horário da programação')
    data_dia = models.ForeignKey(DiasdePalestra)
    participante = models.ForeignKey(Ministrante, default=1)
    evento = models.ForeignKey(Evento, default=1)
    class Meta:
        verbose_name = 'Programação'
        verbose_name_plural = 'Programação'
    def __unicode__(self):
        return '%s - %s' % (self.programa, self.participante.nome)

class GaleriaEvento(models.Model):
    class Meta:
        verbose_name_plural = 'Galleries'
    publicar = models.BooleanField('Publicar', default=True)
    titulo = models.CharField('Title', max_length=100)
    subtitulo = models.CharField('Subtítulo', max_length=200)
    evento = models.ForeignKey(Evento)
    def __str__(self):
        return self.titulo

class Image(models.Model):
    imagem = models.ImageField('File', upload_to='images/')
    galeria = models.ForeignKey(GaleriaEvento, related_name='images_set', blank=True, null=True)

    def __str__(self):
        return self.filename

    @property
    def filename(self):
        return self.galeria.titulo.rsplit('/', 1)[-1]

class FotoCapa(models.Model):
    publicar = models.BooleanField('Publicar', default=True)
    nome = models.CharField('Legenda da foto', max_length=50)
    imagem = models.ImageField('File', upload_to='images/')
    evento = models.ForeignKey(Evento, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Foto de capa'
        verbose_name_plural = 'Fotos de capa'
    def __unicode__(self):
        return self.nome

class Patrocinio(models.Model):
    publicar = models.BooleanField('Publicar', default=True)
    nome = models.CharField('Nome', max_length=30)
    imagem = models.ImageField(upload_to='patrocinador')
    evento = models.ForeignKey(Evento)
    class Meta:
        verbose_name = 'Patrocinador'
        verbose_name_plural = 'Patrocinadores'
    def __unicode__(self):
        return self.nome

class Duvida(models.Model):
    publicar = models.BooleanField('Publicar', default=True)
    pergunta = models.CharField('Pergunta', max_length=100)
    resposta = models.TextField('Resposta')
    evento = models.ForeignKey(Evento)
    class Meta:
        verbose_name = 'Dúvida'
        verbose_name_plural = 'Dúvidas'
    def __unicode__(self):
        return '%s - %s' % (self.pergunta, self.resposta)

class Testemunhal(models.Model):
    publicar = models.BooleanField('Publicar')
    depoimento = models.TextField('Depoimento')
    participante = models.ForeignKey(Pessoa)
    evento = models.ForeignKey(Evento)
    class Meta:
        verbose_name = 'Depoimento'
        verbose_name_plural = 'Depoimentos'
    def __unicode__(self):
        return '%s - %s' % (self.participante.nome, self.evento.nome)

class Noticia(models.Model):
    titulo = models.CharField('Título', max_length=100)
    url = models.URLField('Link', max_length=21, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    evento = models.ForeignKey(Evento)

class Inscricao(models.Model):
    pago = models.BooleanField(default=False)
    pessoa = models.ForeignKey(Participante)
    ingresso = models.ForeignKey(Ingresso)
    evento = models.ForeignKey(Evento)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return '%s - %s' % (self.pessoa.nome, self.evento.nome)
    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify


def evento_pre_save(signal, instance, sender, **kwargs):
    instance.slugevento = slugify(instance.nome) + '-' + slugify(instance.data_evento.year)

signals.pre_save.connect(evento_pre_save, sender=Evento)
