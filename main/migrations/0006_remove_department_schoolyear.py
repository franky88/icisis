# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-01 08:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20170228_0233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='schoolyear',
        ),
    ]