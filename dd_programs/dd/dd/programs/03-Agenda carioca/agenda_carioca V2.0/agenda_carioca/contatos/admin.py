from django.contrib import admin
from agenda_carioca.contatos.models import Contato 
# Register your models here.


class ContatoAdmin(admin.modelAdmin):
	model = Contato
	list_display = ('contato_nome', 'contato_email', 'contato_favorito') #desta ioinformações seram mostradas na tela do admnistrador
	list_filter = ('contato_sexo', 'contato_estado_civil') # para fazer filtr de dados
	search_fields = ('contato_nome', 'contato_sexo')
	save_on_top = True
admin.site.register(Contato, ContatoAdmin)

class TarefaAdmin(admin.modelAdmin):
	model = Tarefa
	list_display = ('tarefa_nome', 'tarefa_data_inicio', 'concluido') #desta ioinformações seram mostradas na tela do admnistrador
	list_filter = ('tarefa_nome') # para fazer filtr de dados
	search_fields = ('tarefa_nome')
	save_on_top = True
admin.site.register(Tarefa, TarefaAdmin)

class ContaAdmin(admin.modelAdmin):
	model = Conta
	list_display = ('conta_nome', 'conta_data_vencimento', 'pago') #desta ioinformações seram mostradas na tela do admnistrador
	list_filter = ('conta_nome') # para fazer filtr de dados
	search_fields = ('conta_nome')
	save_on_top = False
admin.site.register(Conta, ContaAdmin)
