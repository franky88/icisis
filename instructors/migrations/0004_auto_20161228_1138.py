# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-28 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0003_instructor_employment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='id_number',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]