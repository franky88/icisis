# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-13 04:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20161213_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='strand',
            name='strand',
            field=models.CharField(default='ICT', max_length=60),
        ),
    ]
