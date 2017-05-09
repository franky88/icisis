# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-13 01:55
from __future__ import unicode_literals

from django.db import migrations, models
import instructors.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=15)),
                ('first_name', models.CharField(max_length=60)),
                ('middle_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('extension_name', models.CharField(max_length=5)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=6)),
                ('birth_date', models.DateField()),
                ('email_add', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=15)),
                ('adddress', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=instructors.models.upload_location)),
            ],
        ),
    ]
