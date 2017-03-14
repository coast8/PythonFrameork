# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='Nome', max_length=100)),
                ('slug', models.SlugField(verbose_name='Identificador', max_length=100)),
                ('created', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='Modificado em', auto_now=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'ordering': ['name'],
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='Nome', max_length=100)),
                ('slug', models.SlugField(verbose_name='Identificador', max_length=100)),
                ('description', models.TextField(verbose_name='Descrição', blank=True)),
                ('price', models.DecimalField(verbose_name='Preço', decimal_places=2, max_digits=8)),
                ('created', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='Modificado em', auto_now=True)),
                ('category', models.ForeignKey(verbose_name='Categoria', to='catalago.Category')),
            ],
            options={
                'verbose_name': 'Produto',
                'ordering': ['name'],
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
