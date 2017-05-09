# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-06 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0005_auto_20170306_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='descriptive_title',
            field=models.CharField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_code',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]