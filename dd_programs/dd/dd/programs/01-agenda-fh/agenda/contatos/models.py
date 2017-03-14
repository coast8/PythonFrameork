from django.db import models

# Create your models here.


class Contato(models.Model):
	nome = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	telefone = models.CharField(max_length=20)
	sexo = models.CharField(max_length=1)
	cidade = models.CharField(max_length=50, default="Teresina")

	def __str__(self):
		return self.nome