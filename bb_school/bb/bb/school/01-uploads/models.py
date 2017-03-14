class Course(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField(
        'Data de Início', null=True, blank=True
    )

    
    ##fazendo aqui o upload de imagens
    ## depende da biblioteca pillow    --- pip install pillow
    image = models.ImageField(
        upload_to='courses/images', verbose_name='Imagem',
        null=True, blank=True
    )

    ##inseri dados automatico       auto_now_add
    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )

    ##inserção outomatica tbm
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = CourseManager()