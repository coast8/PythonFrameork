from django.db import models
from south.modelsinspector import add_introspection_rules
from django_extensions.db import models as de_models

add_introspection_rules([], ["^django_extensions\.db\.fields\.CreationDateTimeField", "^django_extensions\.db\.fields\.ModificationDateTimeField"])

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

#from django.db import models

def nome_do_produto_da_transacao(sf):
    return Produto.objects.get(id=sf.produto.id).nome + " - " + str(sf.data) + " - " + str(sf.quantidade)

class Categoria(models.Model):
    #id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=135, blank=True)
    class Meta:
        db_table = u'categoria'

    def __unicode__(self):
        return self.nome

class Entrada(de_models.TimeStampedModel):
    #id = models.IntegerField(primary_key=True)
    data = models.DateTimeField()
    categoria = models.ForeignKey(Categoria, db_column="categoria") #max_length=135)
    produto = models.ForeignKey('Produto', db_column="produto")
    fornecedor = models.ForeignKey('Fornecedor', db_column="fornecedor")
    quantidade = models.IntegerField()
    obs = models.TextField()
    class Meta:
        db_table = u'entrada'

    def __unicode__(self):
        #return self.produto
        return nome_do_produto_da_transacao(self)

class Fornecedor(de_models.TimeStampedModel):
    #id = models.IntegerField(primary_key=True)
    nome = models.TextField()
    telefone = models.TextField(blank=True)
    estado = models.TextField(blank=True)
    cidade = models.TextField(blank=True)
    class Meta:
        db_table = u'fornecedor'

    def __unicode__(self):
        return self.nome

class Produto(de_models.TimeStampedModel):
    #id = models.IntegerField(primary_key=True)
    categoria = models.ForeignKey(Categoria, db_column="categoria")
    #categ_rel = models.ForeignKey(Categoria)
    nome = models.TextField()
    estoque_minimo = models.IntegerField()
    estoque_atual = models.IntegerField()
    class Meta:
        db_table = u'produto'

    def __unicode__(self):
        return self.nome

class Retirante(de_models.TimeStampedModel):
    #id = models.IntegerField(primary_key=True)
    nome = models.TextField()
    empresa = models.TextField()
    class Meta:
        db_table = u'retirante'

    def __unicode__(self):
        return self.nome

class Saida(de_models.TimeStampedModel):
    #id = models.IntegerField(primary_key=True)
    data = models.DateTimeField()
    categoria = models.ForeignKey(Categoria, db_column="categoria")
    produto = models.ForeignKey(Produto, db_column="produto")
    retirante = models.ForeignKey(Retirante, db_column="retirante")
    quantidade = models.IntegerField()
    obs = models.TextField()
    class Meta:
        db_table = u'saida'

    def __unicode__(self):
        return nome_do_produto_da_transacao(self)