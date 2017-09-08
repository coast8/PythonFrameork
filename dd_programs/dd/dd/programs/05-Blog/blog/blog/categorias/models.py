from django.db import models

# Create your models here.

class Categoria(models.Model):
	nome = models.CharField(u'Categoria', max_length=70)
	descricao = models.TextField(u'Descrição', blank=True)

	def __str__(self):
		return self.nome