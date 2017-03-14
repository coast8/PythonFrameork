# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComoFunciona',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('titulo', models.CharField(verbose_name='Título da Página', max_length=50)),
                ('descricao', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name_plural': 'Como funciona',
                'verbose_name': 'Como funciona',
            },
        ),
        migrations.CreateModel(
            name='Sobre',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('titulo', models.CharField(verbose_name='Título da Página', max_length=50)),
                ('descricao', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name_plural': 'Sobre',
                'verbose_name': 'Sobre',
            },
        ),
    ]
