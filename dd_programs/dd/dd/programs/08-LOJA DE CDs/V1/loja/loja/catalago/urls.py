from django.conf.urls import url

#example import views
from loja.catalago.views import lista_categorias
from loja.catalago.views import lista_produtos
from loja.catalago.views import categoria
from loja.catalago.views import produto

urlpatterns = [
    url(r'^lista-de-categorias/$', lista_categorias, name='lista_categorias'),
    url(r'^lista-de-produtos/$', lista_produtos, name='lista_produtos'),
    url(r'^categoria/(?P<slug>[\w_-]+)/$', categoria, name='categoria'),
    url(r'^produto/(?P<slug>[\w_-]+)/$', produto, name='produto'),
            #URL-amigavel        #funcao DEF      #variavel p localizar pag. 
    
]
