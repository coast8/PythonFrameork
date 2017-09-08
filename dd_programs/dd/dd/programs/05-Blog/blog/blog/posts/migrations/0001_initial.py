# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('titulo', models.CharField(max_length=150, verbose_name='Título do post')),
                ('descricao_curta', models.TextField(verbose_name='Descrição curta')),
                ('materia', models.TextField(verbose_name='Corpo da matéria')),
                ('tags', models.CharField(max_length=50, verbose_name='Palavra-chave')),
                ('data_post', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
