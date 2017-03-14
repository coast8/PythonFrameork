from django.conf.urls import url

from multirao.core.views import home, cadastro_usuario, sucesso_usuario,\
user_login, sobre, como_funciona, user_logout

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^cadastro-usuario/$', cadastro_usuario, name='cadastrousuario'),
    url(r'^login/$', user_login, name='userlogin'),
    url(r'^logout/$', user_logout, name='userlogout'),
    url(r'^sucesso-usuario/$', sucesso_usuario, name='usuariosucesso'),
    url(r'^sobre/$', sobre, name='sobre'),
    url(r'^como-funciona/$', como_funciona, name='comofunciona'),
]
