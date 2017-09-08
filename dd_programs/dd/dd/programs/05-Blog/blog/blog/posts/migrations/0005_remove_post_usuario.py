# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='usuario',
        ),
    ]
