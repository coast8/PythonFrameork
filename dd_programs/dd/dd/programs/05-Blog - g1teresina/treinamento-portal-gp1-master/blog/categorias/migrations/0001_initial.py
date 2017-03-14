# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70, verbose_name='Categoria')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
            ],
        ),
    ]
