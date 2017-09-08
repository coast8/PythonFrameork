from django.contrib import admin

from .models import Contatos 
# criando as ktabelas do database


class ContatosAdmin(admin.ModelAdmin):
	list_display = ('nome', 'email', 'telefone', 'sexo', 'cidade')
	search_fields = ('nome', 'email')

admin.site.register(Contatos, ContatosAdmin)

