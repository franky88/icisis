# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-13 04:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0002_auto_20161213_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='employment_status',
            field=models.CharField(choices=[('Part time', 'Part time'), ('Full time', 'Full time'), ('Probetionary', 'Probetionary'), ('Regular', 'Regular')], default='Part time', max_length=13),
        ),
    ]
