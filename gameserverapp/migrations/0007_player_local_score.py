# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-07 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameserverapp', '0006_auto_20160905_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='local_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
