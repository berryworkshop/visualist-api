# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 03:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170913_0246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('vocabulary', models.CharField(choices=[('AAT', 'Getty Art and Architecture Thesaurus'), ('LOC', 'Library of Congress Subject Headings'), ('ISO 3166-1', 'ISO Country Names'), ('ISO 3166-2', 'ISO Subdivision Names')], max_length=25)),
                ('value', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'terms',
                'ordering': ['vocabulary', 'value'],
            },
        ),
        migrations.AlterField(
            model_name='address',
            name='address_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Term'),
        ),
        migrations.AlterField(
            model_name='person',
            name='nationalities',
            field=models.ManyToManyField(blank=True, to='api.Term'),
        ),
        migrations.DeleteModel(
            name='Nationality',
        ),
        migrations.AlterUniqueTogether(
            name='term',
            unique_together=set([('vocabulary', 'value')]),
        ),
    ]
