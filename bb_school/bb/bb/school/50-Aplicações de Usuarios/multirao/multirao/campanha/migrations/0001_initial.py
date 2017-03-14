# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campanha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Campanha')),
                ('descricao', models.TextField(verbose_name='Finalidade')),
                ('local', models.CharField(max_length=250, verbose_name='Local')),
                ('data_campanha', models.DateField(verbose_name='Data')),
                ('horario', models.TimeField(verbose_name='Horário')),
                ('imagem', models.ImageField(verbose_name='Imagem', upload_to='uploads')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
