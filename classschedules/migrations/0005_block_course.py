# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-02 04:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_department_schoolyear'),
        ('classschedules', '0004_schedule_block'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Course'),
        ),
    ]