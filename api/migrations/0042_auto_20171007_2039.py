# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 20:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0041_auto_20171007_2022'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='recordsource',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='recordsource',
            name='record',
        ),
        migrations.RemoveField(
            model_name='recordsource',
            name='source',
        ),
        migrations.RemoveField(
            model_name='record',
            name='sources',
        ),
        migrations.RemoveField(
            model_name='relation',
            name='sources',
        ),
        migrations.AddField(
            model_name='relation',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Source'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Source'),
        ),
        migrations.DeleteModel(
            name='RecordSource',
        ),
    ]
