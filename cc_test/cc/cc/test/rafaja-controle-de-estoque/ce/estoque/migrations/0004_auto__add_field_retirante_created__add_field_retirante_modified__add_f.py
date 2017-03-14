# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Retirante.created'
        db.add_column(u'retirante', 'created', self.gf('django_extensions.db.fields.CreationDateTimeField')(default=datetime.datetime.now, blank=True), keep_default=False)

        # Adding field 'Retirante.modified'
        db.add_column(u'retirante', 'modified', self.gf('django_extensions.db.fields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True), keep_default=False)

        # Adding field 'Fornecedor.created'
        db.add_column(u'fornecedor', 'created', self.gf('django_extensions.db.fields.CreationDateTimeField')(default=datetime.datetime.now, blank=True), keep_default=False)

        # Adding field 'Fornecedor.modified'
        db.add_column(u'fornecedor', 'modified', self.gf('django_extensions.db.fields.ModificationDateTimeField')(default=datetime.datetime.now, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Retirante.created'
        db.delete_column(u'retirante', 'created')

        # Deleting field 'Retirante.modified'
        db.delete_column(u'retirante', 'modified')

        # Deleting field 'Fornecedor.created'
        db.delete_column(u'fornecedor', 'created')

        # Deleting field 'Fornecedor.modified'
        db.delete_column(u'fornecedor', 'modified')


    models = {
        'estoque.categoria': {
            'Meta': {'object_name': 'Categoria', 'db_table': "u'categoria'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '135', 'blank': 'True'})
        },
        'estoque.entrada': {
            'Meta': {'object_name': 'Entrada', 'db_table': "u'entrada'"},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estoque.Categoria']", 'db_column': "'categoria'"}),
            'created': ('django_extensions.db.fields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'data': ('django.db.models.fields.DateTimeField', [], {}),
            'fornecedor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estoque.Fornecedor']", 'db_column': "'fornecedor'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django_extensions.db.fields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'obs': ('django.db.models.fields.TextField', [], {}),
            'produto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estoque.Produto']", 'db_column': "'produto'"}),
            'quantidade': ('django.db.models.fields.IntegerField', [], {})
        },
        'estoque.fornecedor': {
            'Meta': {'object_name': 'Fornecedor', 'db_table': "u'fornecedor'"},
            'cidade': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django_extensions.db.fields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'estado': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django_extensions.db.fields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nome': ('django.db.models.fields.TextField', [], {}),
            'telefone': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'estoque.produto': {
            'Meta': {'object_name': 'Produto', 'db_table': "u'produto'"},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estoque.Categoria']", 'db_column': "'categoria'"}),
            'created': ('django_extensions.db.fields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'estoque_atual': ('django.db.models.fields.IntegerField', [], {}),
            'estoque_minimo': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django_extensions.db.fields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nome': ('django.db.models.fields.TextField', [], {})
        },
        'estoque.retirante': {
            'Meta': {'object_name': 'Retirante', 'db_table': "u'retirante'"},
            'created': ('django_extensions.db.fields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django_extensions.db.fields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nome': ('django.db.models.fields.TextField', [], {})
        },
        'estoque.saida': {
            'Meta': {'object_name': 'Saida', 'db_table': "u'saida'"},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estoque.Categoria']", 'db_column': "'categoria'"}),
            'created': ('django_extensions.db.fields.CreationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'data': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django_extensions.db.fields.ModificationDateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'obs': ('django.db.models.fields.TextField', [], {}),
            'produto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estoque.Produto']", 'db_column': "'produto'"}),
            'quantidade': ('django.db.models.fields.IntegerField', [], {}),
            'retirante': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estoque.Retirante']", 'db_column': "'retirante'"})
        }
    }

    complete_apps = ['estoque']