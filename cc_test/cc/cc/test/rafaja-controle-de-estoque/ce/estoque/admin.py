from django.contrib import admin
from estoque.models import *

class EntradaAdmin(admin.ModelAdmin):
    list_display = ('data', 'produto', 'quantidade')
    list_filter = ('produto','created','modified','data')
    date_hierarchy = 'data'

class SaidaAdmin(admin.ModelAdmin):
    list_display = ('data', 'produto', 'retirante', 'quantidade')
    list_filter = ('retirante','created','modified','data')
    date_hierarchy = 'data'

admin.site.register(Categoria)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Fornecedor)
admin.site.register(Produto)
admin.site.register(Retirante)
admin.site.register(Saida, SaidaAdmin)
