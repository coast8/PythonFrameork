from django.conf.urls import url

from mutirao.core.views import home
from mutirao.core.views import cadastro_usuario
from mutirao.core.views import sucesso_usuario
from mutirao.core.views import user_login
from mutirao.core.views import user_logout 

urlpatterns = [
    url(r'^$', home, name='home'),
            #URL-amigavel        #funcao DEF      #variavel p localizar pag. 
    url(r'^cadastro-usuario/$', cadastro_usuario, name='cadastrousuario'),
    url(r'^sucesso-usuario/$', sucesso_usuario, name='usuariosucesso'),
    url(r'^login/$', user_login, name='userlogin'),
    url(r'^logout/$', user_logout, name='userlogout'),
    ]
