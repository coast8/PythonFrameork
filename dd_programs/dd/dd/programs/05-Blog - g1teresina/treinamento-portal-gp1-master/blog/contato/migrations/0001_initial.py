# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_pagina', models.CharField(verbose_name='Título', max_length=50)),
                ('informacoes', models.TextField(verbose_name='Informações de contato')),
            ],
        ),
    ]
