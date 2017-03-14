# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Categoria'
        db.create_table(u'categoria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=135, blank=True)),
        ))
        db.send_create_signal('estoque', ['Categoria'])

        # Adding model 'Entrada'
        db.create_table(u'entrada', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data', self.gf('django.db.models.fields.DateTimeField')()),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estoque.Categoria'], db_column='categoria')),
            ('produto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estoque.Produto'], db_column='produto')),
            ('fornecedor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estoque.Fornecedor'], db_column='fornecedor')),
            ('quantidade', self.gf('django.db.models.fields.IntegerField')()),
            ('obs', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('estoque', ['Entrada'])

        # Adding model 'Fornecedor'
        db.create_table(u'fornecedor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.TextField')()),
            ('telefone', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('estado', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('cidade', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('estoque', ['Fornecedor'])

        # Adding model 'Produto'
        db.create_table(u'produto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estoque.Categoria'], db_column='categoria')),
            ('nome', self.gf('django.db.models.fields.TextField')()),
            ('estoque_minimo', self.gf('django.db.models.fields.IntegerField')()),
            ('estoque_atual', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('estoque', ['Produto'])

        # Adding model 'Retirante'
        db.create_table(u'retirante', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.TextField')()),
            ('empresa', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('estoque', ['Retirante'])

        # Adding model 'Saida'
        db.create_table(u'saida', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data', self.gf('django.db.models.fields.DateTimeField')()),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estoque.Categoria'], db_column='categoria')),
            ('produto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estoque.Produto'], db_column='produto')),
            ('retirante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estoque.Retirante'], db_column='retirante')),
            ('quantidade', self.gf('django.db.models.fields.IntegerField')()),
            ('obs', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('estoque', ['Saida'])


    def backwards(self, orm):
        
        # Deleting model 'Categoria'
        db.delete_table(u'categoria')

        # Deleting model 'Entrada'
        db.delete_table(u'entrada')

        # Deleting model 'Fornecedor'
        db.delete_table(u'fornecedor')

        # Deleting model 'Produto'
        db.delete_table(u'produto')

        # Deleting model 'Retirante'
        db.delete_table(u'retirante')

        # Deleting model 'Saida'
        db.delete_table(u'saida')


    models = {
        'estoque.categoria': {
            'Meta': {'object_name': 'Categoria', 'db_table': "u'categoria'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '135', 'blank': 'True'})
        },
        'estoque.entrada': {
            'Meta': {'object_name': 'Entrada', 'db_table': "u'entrada'"},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estoque.Categoria']", 'db_column': "'categoria'"}),
            'data': ('django.db.models.fields.DateTimeField', [], {}),
            'fornecedor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estoque.Fornecedor']", 'db_column': "'fornecedor'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obs': ('django.db.models.fields.TextField', [], {}),
            'produto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estoque.Produto']", 'db_column': "'produto'"}),
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
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estoque.Categoria']", 'db_column': "'categoria'"}),
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
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estoque.Categoria']", 'db_column': "'categoria'"}),
            'data': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obs': ('django.db.models.fields.TextField', [], {}),
            'produto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estoque.Produto']", 'db_column': "'produto'"}),
            'quantidade': ('django.db.models.fields.IntegerField', [], {}),
            'retirante': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estoque.Retirante']", 'db_column': "'retirante'"})
        }
    }

    complete_apps = ['estoque']
