# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 04:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_recordtimespace_duration_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recordtimespace',
            name='properties',
        ),
    ]
