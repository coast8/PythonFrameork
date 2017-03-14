# -*- coding: utf-8 -*-
__author__ = 'juniorlima'

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.contrib.sitemaps import ping_google
from django.core.exceptions import ValidationError

from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField

from cadastro.models import Proprietario
from sitio.folder_image import destino_foto_propriedade, destino_imagem_propriedade
from core.choices import TIPO_COBRANCA_PROPRIEDADE

#CARACTERISTICAS DO IMOVEL
class TipoImovel(models.Model):
    ativo = models.BooleanField('Ativo', default=True)
    nome = models.CharField('Nome do tipo do imóvel', max_length=20, unique=True)
    descricao = models.CharField('Descrição', max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=25, blank=True, unique=True)
    class Meta:
        verbose_name = 'Tipo de Imóvel'
        verbose_name_plural = 'Tipo de Imóveis'
    def __unicode__(self):
        return self.nome

class TipoOperacao(models.Model):
    ativo = models.BooleanField('Ativo', default=True)
    nome = models.CharField('Nome da operação', max_length=20, unique=True)
    slug = models.SlugField(max_length=25, blank=True, unique=True)
    class Meta:
        verbose_name = 'Tipo de Operação'
        verbose_name_plural = 'Tipo de Operação'
    def __unicode__(self):
        return self.nome

class TipoEvento(models.Model):
    ativo = models.BooleanField('Ativo', default=True)
    nome = models.CharField('Nome', max_length=30, unique=True)
    descricao = models.CharField('Descrição', max_length=200)
    slugtipoevento = models.SlugField(max_length=30, editable=False)
    class Meta:
        verbose_name = 'Tipo de Evento'
        verbose_name_plural = 'Tipo de Eventos'
    def __unicode__(self):
        return self.nome

#CARACTERISTICAS DE LOCALIZAÇÃO
class Estado(models.Model):
    sigla = models.CharField('Sigla', max_length=2, unique=True)
    nome = models.CharField('Estado', max_length=20, unique=True)
    slugsigla = models.CharField('Sigla', max_length=2, unique=True, blank=True)
    def __unicode__(self):
        return '%s - %s' % (self.sigla, self.nome)
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

class Cidade(models.Model):
    nome = models.CharField('Cidade', max_length=50, unique=True)
    uf = models.ForeignKey(Estado, verbose_name='Estado')
    slugcidade = models.SlugField(max_length=100, blank=True, unique=True)
    def __unicode__(self):
        return '%s %s' % (self.nome, self.uf)
    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        unique_together = (("nome", "uf"),)
    def url_sitemap(self):
        tipos = TipoEvento.objects.all()
        for tipo in tipos:
            tiposlug = tipo.slugtipoevento
            #print '%s/%s/%s' % (self.uf.slugsigla, self.slugcidade, tiposlug)
        return reverse('rest.views.cidadetipo', kwargs={'slugcidade':self.slugcidade,
                                                        'sluguf': self.uf.slugsigla,
                                                        'slugtipo': tiposlug,
        })
    def get_absolute_url(self):
        return reverse('rest.views.uf_cidade', kwargs={'sluguf':self.uf.slugsigla,
                                                       'slugcidade': self.slugcidade,
        })
class Zona(models.Model):
    publicar = models.BooleanField('Publicar', default=True)
    nome = models.CharField('Nome da zona', max_length=20)
    localizacao = models.CharField('Localização', max_length=50)
    cidade_uf = models.ForeignKey(Cidade, verbose_name='Cidade Estado')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, blank=True, unique=True)
    def __unicode__(self):
        return '%s - %s' % (self.nome, self.cidade_uf.nome)

class Propriedade(models.Model):
    publicar = models.BooleanField('Publicar', default=True)
    destaque = models.BooleanField('Destaque', default=True)
    nome = models.CharField('Nome', max_length=100)
    ficticio = models.CharField('Nome Fictício do Sítio', max_length=100, help_text='Nome do sítio que aparecerá no site', blank=True, null=True,unique=True)
    proprietario = models.ForeignKey(Proprietario, related_name='propriedade_set', verbose_name='Proprietário')

    operacao = models.ForeignKey(TipoOperacao, verbose_name="Operação")
    categoria = models.ForeignKey(TipoImovel)
    tipoevento = models.ManyToManyField(TipoEvento, verbose_name='Tipo de Evento', related_name='evento_prop')
    zona = models.ForeignKey(Zona, blank=True, null=True)

    resumo_sitio = models.CharField('Descreva a chamada do sítio no site', max_length=100)
    descricao = RichTextField('Descrição no site', config_name='default', default='Informações sobre o sítio')
    informacao_cliente = RichTextField('Informações para cliente', config_name='default', blank=True, null=True)
    dados_negociacao = RichTextField('Informações para negociação', config_name='default', blank=True, null=True)
    dados_especificos = RichTextField('Dados específicos de contrato', config_name='default', blank=True, null=True)

    localizacao = models.CharField('Localização', max_length=200, blank=True, null=True)

    telefone = models.CharField('Telefone', max_length=14, blank=True, null=True)
    site = models.URLField('Site', max_length=100, blank=True, null=True)
    email = models.EmailField('Email', max_length=50, blank=True, null=True)

    # Estrutura
    quartos = models.PositiveSmallIntegerField('Quartos',)
    pessoas = models.PositiveSmallIntegerField('Nº Máximo de pessoas',)
    banheiros = models.PositiveSmallIntegerField('Banheiros',)
    capacidadeevento = models.PositiveSmallIntegerField('Capacidade do local para eventos', blank=True, null=True)
    capacidadepernoite = models.PositiveSmallIntegerField('Capacidade do local para pernoite', blank=True, null=True)

    # Acomodação
    casasede = models.BooleanField('Casa Sede', default=False)
    casa = models.BooleanField('Casa', default=True)
    casaduplex = models.BooleanField('Casa Duplex', default=False)
    chale = models.BooleanField('Chalé', default=False)
    murado = models.BooleanField('Muros', default=False)
    mobiliado = models.BooleanField('Mobiliado', default=False)

    # Espaços
    alojamento = models.BooleanField('Alojamento', default=False)
    banheiro = models.BooleanField('Banheiro', default=False)
    vestiariofeminino = models.BooleanField('Vestiário Feminino', default=False)
    vestiariomasculino = models.BooleanField('Vestiário Masculino', default=False)
    sala = models.BooleanField('Sala', default=False)
    bercario = models.BooleanField('Berçário', default=False)
    capela = models.BooleanField('Capela', default=False)
    estacionamento = models.BooleanField('Estacionamento', default=False)

    # Lazer
    salaodefesta = models.BooleanField('Salão de Festa', default=False)
    salaodeculto = models.BooleanField('Sala de Culto', default=False)
    salasdereunioes = models.BooleanField('Sala de Reuniões', default=False)

    # Cozinha
    cozinhacomum = models.BooleanField('Cozinha Comum', default=False)
    cozinhaindustrial = models.BooleanField('Cozinha Industrial', default=False)
    restaurante = models.BooleanField('Restaurante', default=False)
    alimentacao = models.BooleanField('Alimentação', default=False)
    freezer = models.BooleanField('Freezer', default=False)
    bar = models.BooleanField('Bar', default=False)
    geladeira = models.BooleanField('Geladeira', default=False)
    microondas = models.BooleanField('Microondas', default=False)
    fogao = models.BooleanField('Fogão', default=False)
    churrasqueira = models.BooleanField('Churrasqueira', default=False)

    # Quartos
    suite = models.BooleanField('Suíte', default=False)
    quarto = models.BooleanField('Quarto', default=False)
    armador = models.BooleanField('Armador para redes', default=False)

    # Lazer
    areadeservico = models.BooleanField('Área de Serviço', default=False)
    campodefutebol = models.BooleanField('Campo de Futebol', default=False)
    campodevolei = models.BooleanField('Campo de Vôlei', default=False)
    campodegolf = models.BooleanField('Campo de Golf', default=False)
    quadrapoliesportiva = models.BooleanField('Quadra Poliesportiva', default=False)
    quadradetenis = models.BooleanField('Quadra de Tênis', default=False)
    piscinaadulto = models.BooleanField('Piscina Adulto', default=True)
    piscinainfantil = models.BooleanField('Piscina Intantil', default=False)
    playground = models.BooleanField('Playground', default=False)
    cadeirante = models.BooleanField('Acesso para cadeira de rodas', default=False)

    # Acessórios
    som = models.BooleanField('Som', default=False)
    sinuca = models.BooleanField('Sinuca', default=False)
    pingpong = models.BooleanField('Mesa Ping pong', default=False)
    dvd = models.BooleanField('DVD', default=False)
    tv = models.BooleanField('TV', default=False)
    internet = models.BooleanField('Acesso a internet', default=False)

    # Espaços
    trilha = models.BooleanField('Trilha para caminhada', default=False)
    lago = models.BooleanField('Lago', default=False)
    cachoeira = models.BooleanField('Cachoeira', default=False)
    praia = models.BooleanField('Praia', default=False)
    bosque = models.BooleanField('Bosque', default=False)
    zoologico = models.BooleanField('Zoológico', default=False)
    parque = models.BooleanField('Parque', default=False)
    jardim = models.BooleanField('Jardim', default=False)

    imagem = ImageField('Imagem do sítio', upload_to=destino_foto_propriedade)

    # Valores
    negociacao = models.BooleanField('Aceita negociação', default=True)
    diaria = models.DecimalField(max_digits=6, decimal_places=2)
    tipodiaria = models.CharField('Tipo de cobrança', max_length=2, default=1, choices=TIPO_COBRANCA_PROPRIEDADE)
    lucro = models.PositiveSmallIntegerField(default=20, help_text='%', blank=True, null=True)
    valorfinal = models.DecimalField('Valor', max_digits=6, decimal_places=2, blank=True, null=True)

    # Feriados
    carnaval = models.BooleanField('Carnaval', default=True)
    semana_santa = models.BooleanField('Semana Santa', default=True)
    reveillon = models.BooleanField('Reveillon', default=True)
    outro = models.BooleanField('Outro feriado', default=True)

    slug = models.SlugField(max_length=100, blank=True, unique=True, editable=False)
    cliques = models.IntegerField('Cliques', default=0, editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, related_name='user_add_%(class)ss', blank=True, null=True)
    usuario_modificou = models.ForeignKey(User, related_name='user_mod_%(class)ss', blank=True, null=True)
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            if not self.capacidadeevento:
                self.capacidadeevento = self.pessoas * 2
            if not self.capacidadepernoite:
                self.capacidadepernoite = self.pessoas * 1.5
        if not self.valorfinal and self.lucro and self.diaria:
            self.valorfinal = self.diaria + (self.diaria*self.lucro/100)
        if not self.lucro and self.valorfinal and self.diaria:
            self.lucro = (self.valorfinal - self.diaria) / self.diaria * 100
        try:
            this = Propriedade.objects.get(id=self.id)
            if this.imagem != self.imagem:
                this.imagem.delete(save=False)
        except: pass # when new photo then we do nothing, normal case
        try:
            ping_google()
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
            pass
        super(Propriedade, self).save()
    def clean(self):
        if not self.id:
            if self.valorfinal is not None and self.lucro is not None:
                raise ValidationError('Apague o VALOR FINAL ou LUCRO')

    def __unicode__(self):
        return "%s - %s" % (self.nome, self.proprietario.apelido)
    class Meta:
        verbose_name = 'Cadastro de Sítio'
        verbose_name_plural = 'Cadastro de Sítios'

# Pre Save
def nome_ficticio_pre_save(signal, instance, sender, **kwargs):
    print 'entrou ?'
    if not instance.ficticio:
        print 'entrou'
        instance.ficticio = instance.nome
    instance.slug = slugify(instance.ficticio)
signals.pre_save.connect(nome_ficticio_pre_save, sender=Propriedade)

def operacao_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(operacao_pre_save, sender=TipoOperacao)

def tipo_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.nome)

signals.pre_save.connect(tipo_pre_save, sender=TipoImovel)

def zona_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(zona_pre_save, sender=Zona)

def cidade_pre_save(signal, instance, sender, **kwargs):
    instance.slugcidade = slugify(instance.nome)

signals.pre_save.connect(cidade_pre_save, sender=Cidade)

def sigla_pre_save(signal, instance, sender, **kwargs):
    instance.slugsigla = slugify(instance.sigla)

signals.pre_save.connect(sigla_pre_save, sender=Estado)