from django.conf.urls import url

from agenda.contatos.views import add_contato, cadastro_sucesso, lista_contatos,\
apagar_contato, editar_contato

urlpatterns = [
	url(r'^adicionar-contato/$', add_contato, name='addcontato'),
	url(r'^sucesso/$', cadastro_sucesso, name='sucesso'),
	url(r'^lista-contatos/$', lista_contatos, name='listacontatos'),
	url(r'^deletar-contato/(?P<id>\d+)/$', apagar_contato, name='apagarcontato'),
	url(r'^editar-contato/(?P<id>\d+)/$', editar_contato, name='editarcontato'),
]
