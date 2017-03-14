from django.db import models


"""
    para a função funcionar temos que dar esse import
"""
from django.core.urlresolvers import reverse


class Category(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    #meta informações a respeito do modelo
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']



    """
        PARA O ABSOLTE URL
    """
    def get_absolute_url(self):
        return reverse('catalog:category', kwargs={'slug': self.slug})


========================================================================================
def category(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        'current_category': category,
        'product_list': Product.objects.filter(category=category),
    }
    return render(request, 'catalog/category.html', context)




========================================================================================

url(r'^(?P<slug>[\w_-]+)/$', views.category, name='category'),


==============================================================

{% for category in categories %}
    <li><a href="{{ category.get_absolute_url }}">{{ category }}</a></li>
{% endfor %}