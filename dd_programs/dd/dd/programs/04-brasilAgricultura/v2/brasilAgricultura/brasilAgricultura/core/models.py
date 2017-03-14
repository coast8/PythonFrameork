
from django.db import models
from django.contrib.auth.models import User


class Contato(models.Model):
	nome = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	mensagem = models.CharField(max_length=200)
	
	def __str__(self):
		return self.nome


class Cliente(models.Model):
	nomeCompleto= models.CharField(max_length=50)
	endereco = models.CharField(max_length=50)
	cidade = models.CharField(max_length=50)
	cpf = models.CharField(max_length=50)
	dataNascimento = models.CharField(max_length=200)
	
	def __str__(self):
		return self.nomeCompleto
