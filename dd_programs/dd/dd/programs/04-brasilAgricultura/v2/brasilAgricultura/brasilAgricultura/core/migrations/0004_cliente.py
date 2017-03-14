# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151002_0045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nomeCompleto', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=50)),
                ('dataNascimento', models.CharField(max_length=200)),
            ],
        ),
    ]
