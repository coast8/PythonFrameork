from django.db import models


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

    objects = CourseManager()

    def __str__(self):
        return self.name

#usando o verbose_nane  ele que mudar valores de front-end do admin
    class Meta:
        verbose_name = 'Curso' #exibição da classe
        verbose_name_plural = 'Cursos' #nome no plural
        ordering = ['name'] #ordem de exebição