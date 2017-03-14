from django.contrib import admin
from agenda.contato.models import Contato

# Register your models here.

# vai posssibilitar usar o Django Admin
# e conseguir cadastra um contato.

class ContatoAdmin(admin.modelAdmin):
	model = Contato
	list_display = ['contato_nome', 'contato_email', 'contato_favorito'] #desta ioinformações seram mostradas na tela do admnistrador
	list_filter = ['contato_sexo', 'contato_estado_civil'] # para fazer filtr de dados
	search_fields = ['contato_nome']
	save_on_top = True
admin.site.register(Contato, ContatoAdmin)