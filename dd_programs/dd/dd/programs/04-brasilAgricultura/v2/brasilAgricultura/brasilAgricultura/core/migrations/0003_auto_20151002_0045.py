# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151001_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='mensagem',
            field=models.CharField(max_length=200),
        ),
    ]
