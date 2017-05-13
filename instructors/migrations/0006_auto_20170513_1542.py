# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-13 07:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0005_instructor_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmploymentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='instructor',
            name='employment_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructors.EmploymentStatus'),
        ),
    ]
