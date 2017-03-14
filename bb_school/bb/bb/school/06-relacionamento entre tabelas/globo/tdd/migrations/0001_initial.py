# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nome', models.CharField(verbose_name='Nome do CArro', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nome', models.CharField(verbose_name='Categoria', max_length=70)),
                ('pais', models.TextField(verbose_name='Descrição', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='carro',
            name='fabricante',
            field=models.ForeignKey(to='tdd.Fabricante'),
        ),
    ]
