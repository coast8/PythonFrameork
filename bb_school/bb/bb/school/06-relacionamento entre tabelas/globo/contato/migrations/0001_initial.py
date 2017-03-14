# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('titulo_pagina', models.CharField(max_length=50, verbose_name='Título')),
                ('informacoes', models.TextField(verbose_name='Informações de contato')),
            ],
        ),
    ]
