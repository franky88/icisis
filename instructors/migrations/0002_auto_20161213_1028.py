# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-13 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='extension_name',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
