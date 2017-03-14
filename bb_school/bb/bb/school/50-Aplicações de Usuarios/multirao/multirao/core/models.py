from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	telefone = models.CharField(u'Celular', max_length=14, help_text='(99)99999-9999')
	foto = models.ImageField(upload_to="media/profile", blank=True)
	data_cadastro = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s %s" % (self.user.first_name, self.user.last_name)

class Sobre(models.Model):
	titulo = models.CharField(u'Título da Página', max_length=50)
	descricao = models.TextField(u'Descrição')

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name='Sobre'
		verbose_name_plural='Sobre'

class ComoFunciona(models.Model):
	titulo = models.CharField(u'Título da Página', max_length=50)
	descricao = models.TextField(u'Descrição')

	def __str__(self):
		return self.titulo
	
	class Meta:
		verbose_name='Como funciona'
		verbose_name_plural='Como funciona'