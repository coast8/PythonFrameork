from django.contrib import admin

# Register your models here.


from .models import Contato 
# criando as ktabelas do database


class ContatoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'email', 'telefone', 'sexo', 'cidade')
	search_fields = ('nome', 'email')

admin.site.register(Contato, ContatoAdmin)