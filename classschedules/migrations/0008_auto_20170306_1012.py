# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-06 02:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classschedules', '0007_remove_subjectfee_miscellaneous_fees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjectfee',
            name='subject',
        ),
        migrations.DeleteModel(
            name='SubjectFee',
        ),
    ]
