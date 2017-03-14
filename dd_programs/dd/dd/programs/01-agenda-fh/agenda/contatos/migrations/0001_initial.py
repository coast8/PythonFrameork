# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contatos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
                ('sexo', models.CharField(max_length=1)),
                ('cidade', models.CharField(max_length=50, default='Teresina')),
            ],
        ),
    ]
