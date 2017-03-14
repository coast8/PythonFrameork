# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_auto_20160108_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='usuario',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
    ]
