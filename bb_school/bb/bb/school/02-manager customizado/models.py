#alterando  a  forma de pesquisa do django

from django.db import models


#criando a classe para mudar a forma de pesquisa
# no final do codigo estar o novo valor a objects
class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
        )


class Course(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField(
        'Data de Início', null=True, blank=True
    )

    
    image = models.ImageField(
        upload_to='courses/images', verbose_name='Imagem',
        null=True, blank=True
    )

    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

#dando um novo valor ao 'objects'
    objects = CourseManager()