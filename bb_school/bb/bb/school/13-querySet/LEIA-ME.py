aprendendo a usar as queryset



#  Criando o primeiro Manager
class HistoricoManager(models.Manager):
	#retorna a QuerySet padrão toda
	#vez que um método do Manager é chamado para ser passado a ela
	
	def get_query_set(self):
		query_set = super(HistoricoManager, self).get_query_set()
		return query_set.extra(
			select = {'_valor_total': """select sum(valor) from contas_conta
			where contas_conta.historico_id = contas_historico.id""",
				}
			)

class Historico(models.Model):
	descricao = models.CharField(max_length=50)

	class Meta:
		verbose_name = 'Historico'
		verbose_name_plural = 'Historicos'
		ordering = ['descricao']

	def __str__(self):
		return self.descricao
	
	objects = HistoricoManager()

	def valor_total(self):
		return self._valor_total or 0.0