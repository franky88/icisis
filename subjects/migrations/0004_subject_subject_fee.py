# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-06 02:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_subjectfee'),
        ('subjects', '0003_auto_20170301_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subject_fee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.SubjectFee'),
        ),
    ]
