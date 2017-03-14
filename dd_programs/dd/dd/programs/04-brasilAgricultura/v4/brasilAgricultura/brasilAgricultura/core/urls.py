
##
## essa impotação ja é padrão
from django.conf.urls import url

## funções def que estamos importando 
from brasilAgricultura.core.views import index
from brasilAgricultura.core.views import quemsomos
from brasilAgricultura.core.views import produtos
from brasilAgricultura.core.views import contatos
from brasilAgricultura.core.views import extras
from brasilAgricultura.core.views import sucesso_usuario
from brasilAgricultura.core.views import clientes
from brasilAgricultura.core.views import noticias
from brasilAgricultura.core.views import pg404
from brasilAgricultura.core.views import pg500
from brasilAgricultura.core.views import cadastro
from brasilAgricultura.core.views import sucesso_cliente


urlpatterns = [
    url(r'^$', index, name='index'),

    #URL-amigavel        #funcao DEF   #variavel p localizar pag. 
    url(r'^quem-somos/$', quemsomos, name='quemsomos'),
    url(r'^produtos/$', produtos, name='produtos'),
    url(r'^contatos/$', contatos, name='contatos'),
    url(r'^extras-/$', extras, name='extras'),
    url(r'^sucesso-usuario/$', sucesso_usuario, name='sucesso_usuario'),
    url(r'^lista-clientes/$', clientes, name='clientes'),
    url(r'^noticias-/$', noticias, name='noticias'),
    url(r'^error-/$', pg404, name='pg404'),
    url(r'^erro-/$', pg500, name='pg500'),
    url(r'^novo-cliente/$', cadastro, name='cadastro'),
    url(r'^parabens-novo-cliente/$', sucesso_cliente, name='sucesso_cliente'),
    ]

