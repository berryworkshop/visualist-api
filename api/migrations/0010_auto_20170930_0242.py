# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 02:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20170929_1204'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='record',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
