# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-06 01:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_auto_20170301_1658'),
        ('classschedules', '0005_block_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_fee', models.FloatField()),
                ('miscellaneous_fees', models.FloatField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.Subject')),
            ],
        ),
    ]
