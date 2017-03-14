# -*- coding: utf-8 -*-
__author__ = 'Junior Lima'

from django.contrib.auth.models import User
from django.db import models
from django.core.mail import send_mail
from django.db.models import signals

from lib.ckeditor.fields import RichTextField

class BaseNoticiaAbstract(models.Model):
    publicar = models.BooleanField(default=True)
    destaque = models.BooleanField(default=False)
    titulo = models.CharField(max_length=100)
    conteudo = RichTextField('Conteúdo', config_name='juniorlima')
    slug = models.SlugField(max_length=150, blank=True, editable=False)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    cliques = models.IntegerField('Cliques', default=0, editable=False)

    usuario = models.ForeignKey(User, related_name='user_add_%(class)ss', blank=True, null=True)
    usuario_modificou = models.ForeignKey(User, related_name='user_mod_%(class)ss', blank=True, null=True)
    class Meta:
        abstract = True

class Noticia(BaseNoticiaAbstract):
    pass

class BaseNoticiaVideo(models.Model):
    usarVideo = models.BooleanField(default=True)
    video = models.CharField(max_length=15, help_text="fhbTBA64FkU")
    descricaovideo = models.TextField('Descrição do vídeo', blank=True, null=True)
    class Meta:
        abstract = True


# Inclusão de novo usuário por email
def notify_admin(sender, instance, created, **kwargs):
    '''Notifique o administrador de que um novo usuário foi incluído.'''
    if created:
       subject = 'Novo usuário criado'
       message = 'Usuario %s was adicionado no site Juvenis' % instance.username
       from_addr = 'webjuniorlima@gmail.com'
       recipient_list = ('webjuniorlima@gmail.com',)
       send_mail(subject, message, from_addr, recipient_list)

signals.post_save.connect(notify_admin, sender=User)