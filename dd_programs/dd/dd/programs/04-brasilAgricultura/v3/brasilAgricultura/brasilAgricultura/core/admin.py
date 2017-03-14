from django.contrib import admin

from .models import Contato
from .models import Cliente
# Resistrando as classes de medels.
##################################
class ContatoAdmin(admin.ModelAdmin):
  list_display = ('nome', 'email', 'mensagem')
  search_fields = ('nome',)


class ClienteAdmin(admin.ModelAdmin):
  list_display = ('nomeCompleto', 'endereco', 'cidade', 'cpf', 'dataNascimento')
  search_fields = ('nomeCompleto', 'cpf')
  list_filter = ('cidade', 'dataNascimento')


admin.site.register(Contato, ContatoAdmin)
admin.site.register(Cliente, ClienteAdmin)

####################################################
####################################################