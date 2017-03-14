from django.conf.urls import url

from ana.loja.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
    
            #URL-amigavel        #funcao DEF      #variavel p localizar pag. 
    #url(r'^cadastro-usuario/$', cadastro_usuario, name='cadastrousuario'),
    #url(r'^sucesso-usuario/$', sucesso_usuario, name='usuariosucesso'),
    #url(r'^login/$', user_login, name='userlogin'),
    #url(r'^logout/$', user_logout, name='userlogout'),
    ]
