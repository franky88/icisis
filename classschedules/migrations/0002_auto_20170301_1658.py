# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-01 08:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0005_instructor_department'),
        ('students', '0004_auto_20170301_1658'),
        ('classschedules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_name', models.CharField(max_length=120)),
                ('instructor', models.ManyToManyField(to='instructors.Instructor')),
                ('student', models.ManyToManyField(to='students.Student')),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='student',
            field=models.ManyToManyField(to='students.Student'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='subjects.Subject'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='instructors.Instructor'),
        ),
    ]
