# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-02 01:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classschedules', '0002_auto_20170301_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='block',
            name='student',
        ),
    ]
