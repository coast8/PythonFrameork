from django.db import models

# Create your models here.

class Campanha(models.Model):
	titulo = models.CharField(u'Campanha', max_length=100)
	descricao = models.TextField(u'Finalidade')
	local = models.CharField(u'Local', max_length=250)
	data_campanha = models.DateField(u'Data')
	horario = models.TimeField(u'Horário')
	imagem = models.ImageField(u'Imagem', upload_to="uploads")
	data_criacao = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.titulo