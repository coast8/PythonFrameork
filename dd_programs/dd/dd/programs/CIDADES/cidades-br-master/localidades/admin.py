from django.contrib import admin

# Register your models here.

from .models import Cidade, Estado


class EstadoAdmin(admin.ModelAdmin):
	search_fields = ('nome', 'uf',)
	list_display = ('nome', 'uf',)
	save_on_top = True


class CidadeAdmin(admin.ModelAdmin):
	search_fields = ('nome', 'uf',)
	list_display = ('nome', 'estado','populacao','pib','capital')
	list_filter = ['estado','capital',]
	readonly_fields = ('estado','uf','nome','codigo_ibge','gentilico','populacao','area','densidade_demografica','pib','lat','lng','capital',)
	#list_editable = ('capital',)
	save_on_top = True

admin.site.register(Estado, EstadoAdmin)
admin.site.register(Cidade, CidadeAdmin)