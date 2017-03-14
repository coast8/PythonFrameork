from django.conf.urls import url

#example import views
from loja.core.views import index
from loja.core.views import contato

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^contato/$', contato, name='contato'),
            #URL-amigavel        #funcao DEF      #variavel p localizar pag. 
    #url(r'^cadastro-usuario/$', cadastro_usuario, name='cadastrousuario'),
    ]
