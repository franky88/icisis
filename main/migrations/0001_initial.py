# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-13 03:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.CharField(max_length=4)),
                ('end_year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Semister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semister', models.CharField(choices=[('1st Sem', 'First Semester'), ('2nd Sem', 'Second Semister')], max_length=15)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('schoolyear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.SchoolYear')),
            ],
        ),
    ]
