# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20160108_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='imagens'),
        ),
    ]
