# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Produto.categ_rel'
        db.delete_column(u'produto', 'categ_rel_id')

        # Renaming column for 'Produto.categoria' to match new field type.
        db.rename_column(u'produto', 'categoria', 'categoria_id')
        # Changing field 'Produto.categoria'
        db.alter_column(u'produto', 'categoria_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estoque.Categoria']))

        # Adding index on 'Produto', fields ['categoria']
        db.create_index(u'produto', ['categoria_id'])


    def backwards(self, orm):
        
        # Removing index on 'Produto', fields ['categoria']
        db.delete_index(u'produto', ['categoria_id'])

        # Adding field 'Produto.categ_rel'
        db.add_column(u'produto', 'categ_rel', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['estoque.Categoria']), keep_default=False)

        # Renaming column for 'Produto.categoria' to match new field type.
        db.rename_column(u'produto', 'categoria_id', 'categoria')
        # Changing field 'Produto.categoria'
        db.alter_column(u'produto', 'categoria', self.gf('django.db.models.fields.TextField')())


    models = {
        'estoque.categoria': {
            'Meta': {'object_name': 'Categoria', 'db_table': "u'categoria'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '135', 'blank': 'True'})
        },
        'estoque.entrada': {
            'Meta': {'object_name': 'Entrada', 'db_table': "u'entrada'"},
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '135'}),
            'data': ('django.db.models.fields.DateTimeField', [], {}),
            'fornecedor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estoque.Fornecedor']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obs': ('django.db.models.fields.TextField', [], {}),
            'produto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estoque.Produto']"}),
            'quantidade': ('django.db.models.fields.IntegerField', [], {})
        },
        'estoque.fornecedor': {
            'Meta': {'object_name': 'Fornecedor', 'db_table': "u'fornecedor'"},
            'cidade': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'estado': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.TextField', [], {}),
            'telefone': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'estoque.produto': {
            'Meta': {'object_name': 'Produto', 'db_table': "u'produto'"},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estoque.Categoria']"}),
            'estoque_atual': ('django.db.models.fields.IntegerField', [], {}),
            'estoque_minimo': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.TextField', [], {})
        },
        'estoque.retirante': {
            'Meta': {'object_name': 'Retirante', 'db_table': "u'retirante'"},
            'empresa': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.TextField', [], {})
        },
        'estoque.saida': {
            'Meta': {'object_name': 'Saida', 'db_table': "u'saida'"},
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '135'}),
            'data': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obs': ('django.db.models.fields.TextField', [], {}),
            'produto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estoque.Produto']"}),
            'quantidade': ('django.db.models.fields.IntegerField', [], {}),
            'retirante': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estoque.Retirante']"})
        }
    }

    complete_apps = ['estoque']
