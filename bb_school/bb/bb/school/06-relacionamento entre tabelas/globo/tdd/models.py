from django.db import models

# Create your models here.

class Fabricante(models.Model):
	nome = models.CharField(u'Fabricante:', max_length=70)
	pais = models.TextField(u'País:', blank=True)

	def __str__(self):
		return self.nome

class Carro(models.Model):
	nome = models.CharField(u'Nome do CArro', max_length=150)
	fabricante = models.ForeignKey(Fabricante)
	
	def __str__(self):
		return self.nome