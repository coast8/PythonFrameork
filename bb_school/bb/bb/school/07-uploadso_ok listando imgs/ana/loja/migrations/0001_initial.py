# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('description', models.TextField(blank=True, verbose_name='Descrição Simples')),
                ('about', models.TextField(blank=True, verbose_name='Sobre o Curso')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Data de Início')),
                ('image', models.ImageField(blank=True, null=True, upload_to='courses/images', verbose_name='Imagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Curso',
                'ordering': ['name'],
                'verbose_name_plural': 'Cursos',
            },
        ),
    ]
