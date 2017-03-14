from django.db import models
from django.contrib.auth.models import User

from globo.categorias.models import Categoria

# Create your models here.

class Post(models.Model):
	titulo = models.CharField(u'Título do post', max_length=150)
	descricao_curta = models.TextField(u'Descrição curta')
	materia = models.TextField(u'Corpo da matéria')
	imagem = models.ImageField(upload_to='imagens', blank=True)
	categoria = models.ForeignKey(Categoria)
	tags = models.CharField(u'Palavra-chave', max_length=50)
	usuario = models.ForeignKey(User)
	data_post = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.titulo