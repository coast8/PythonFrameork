from django.db import models

# Create your models here.

class Contato(models.Model):
	titulo_pagina = models.CharField(u'Título', max_length=50)
	informacoes = models.TextField(u'Informações de contato')

	def __str__(self):
		return self.titulo_pagina