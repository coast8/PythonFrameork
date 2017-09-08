class Course(models.Model):
    
    ##fazendo aqui o upload de imagens
    ## depende da biblioteca pillow    --- pip install pillow
    image = models.ImageField(
        upload_to='courses/images', verbose_name='Imagem',
        null=True, blank=True
    )

