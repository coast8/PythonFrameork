from django.contrib import admin
from .models import *

class AdminHistorico(admin.ModelAdmin):
	list_display = ['descricao', 'quantidade', 'total']
	search_fields = ['descricao']


class AdminPessoa(admin.ModelAdmin):
	list_display = ['nome', 'telefone']
	search_fields = ['nome', 'telefone']
    #list_filter = ['nome', 'telefone']

class AdminConta(admin.ModelAdmin):
	list_display = (
		'data_vencimento',
		'valor',
		'status',
		'operacao',
		'historico',
		'pessoa',
		)
	
	search_fields = ('descricao',)
	
	list_filter = (
		'data_vencimento',
		'status',
		'operacao',
		'historico',
		'pessoa',
		)

class InlinePagamentoPago(admin.TabularInline):
	model = PagamentoPago

class AdminContaPagar(admin.ModelAdmin):
	list_display = ('data_vencimento','valor','status','historico','pessoa')
	search_fields = ('descricao',)
	list_filter = ('data_vencimento','status','historico','pessoa',)
	exclude = ['operacao',]

	#importando o tabular
	inlines = [InlinePagamentoPago,]




class InlinePagamentoRecebido(admin.TabularInline):
	model = PagamentoRecebido

class AdminContaReceber(admin.ModelAdmin):
	list_display = ('data_vencimento','valor','status','historico','pessoa')
	search_fields = ('descricao',)
	list_filter = ('data_vencimento','status','historico','pessoa',)
	exclude = ['operacao',]

	#importando o tabular
	inlines = [InlinePagamentoRecebido,]

admin.site.register(Pessoa, AdminPessoa)
admin.site.register(Historico, AdminHistorico)
admin.site.register(Conta, AdminConta)
admin.site.register(ContaPagar, AdminContaPagar)
admin.site.register(ContaReceber, AdminContaReceber)