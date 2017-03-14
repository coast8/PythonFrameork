# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.ForeignKey(default=1, to='categorias.Categoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='imagem',
            field=models.ImageField(default=1, upload_to='imagens'),
            preserve_default=False,
        ),
    ]
