

######## models ##############
## Produto
class Entrada(models.Model):
    criado = models.DateTimeField(('Data da Registro'), auto_now_add=True, auto_now=False)
    modificado = models.DateTimeField(auto_now_add=False, auto_now=True)
    atendente = models.ForeignKey(Atendente)
    cliente = models.ForeignKey(Cliente)
    produto = models.ForeignKey(Produto)
    quantidade   = models.DecimalField(max_digits=6, decimal_places=0)
    validade     = models.DateField()
    valorunitario = models.DecimalField(max_digits=6, decimal_places=2)

    #calculando o total
    def total(self):
        return self.quantidade * (self.valorunitario or 0)

######################### end ############




################# admin ###################
class EntradaAdmin(admin.ModelAdmin):
	list_display = ('criado', 'produto', 'quantidade', 'valorunitario', 'total', 'validade', 'atendente')
###################### end #####################