from django.db import models

# Create your models here.

class Estado(models.Model):
	uf = models.CharField(max_length=2)
	nome = models.CharField(max_length=255)


	def __str__(self):
		return self.nome


class Cidade(models.Model):
	"""(Cidade description)"""
	estado = models.ForeignKey(Estado)
	uf = models.CharField( 'UF', max_length=2)
	nome = models.CharField(max_length=255)
	codigo_ibge = models.IntegerField('Código IBGE', null=True, blank=True)
	gentilico = models.CharField('Gentílico', max_length=255, null=True, blank=True)
	populacao = models.IntegerField('População em 2010', null=True, blank=True)
	area = models.DecimalField('Área da unidade territorial (km²)', max_digits=11, decimal_places=2,null=True,blank=True)
	densidade_demografica = models.DecimalField('Densidade demográfica (hab/km²)', max_digits=11, decimal_places=2,null=True,blank=True)
	pib = models.IntegerField('PIB', null=True, blank=True)

	lat = models.CharField('Latitude', max_length=255, null=True, blank=True)
	lng = models.CharField('Longitude', max_length=255, null=True, blank=True)

	capital = models.BooleanField(default=False)


	def __str__(self):
		return self.nome

	def nome_sem_acento(self):
		from django.template.defaultfilters import slugify
		return slugify("%s-%s" % (self.nome,self.estado.uf))