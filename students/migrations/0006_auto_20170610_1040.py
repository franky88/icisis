# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-10 02:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20170525_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Gender'),
        ),
    ]
