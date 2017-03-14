# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('titulo', models.CharField(verbose_name='Título do post', max_length=150)),
                ('descricao_curta', models.TextField(verbose_name='Descrição curta')),
                ('materia', models.TextField(verbose_name='Corpo da matéria')),
                ('imagem', models.ImageField(upload_to='imagens', blank=True)),
                ('tags', models.CharField(verbose_name='Palavra-chave', max_length=50)),
                ('data_post', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(to='categorias.Categoria')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
