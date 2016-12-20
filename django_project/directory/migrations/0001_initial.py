# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-20 05:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.Record')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.record',),
        ),
        migrations.CreateModel(
            name='Hours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('contactitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='directory.ContactItem')),
            ],
            options={
                'abstract': False,
            },
            bases=('directory.contactitem',),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('contactitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='directory.ContactItem')),
            ],
            options={
                'abstract': False,
            },
            bases=('directory.contactitem',),
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('contactitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='directory.ContactItem')),
            ],
            options={
                'abstract': False,
            },
            bases=('directory.contactitem',),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='directory.Entity')),
            ],
            options={
                'abstract': False,
            },
            bases=('directory.entity',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='directory.Entity')),
            ],
            options={
                'abstract': False,
            },
            bases=('directory.entity',),
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('contactitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='directory.ContactItem')),
            ],
            options={
                'abstract': False,
            },
            bases=('directory.contactitem',),
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('contactitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='directory.ContactItem')),
            ],
            options={
                'abstract': False,
            },
            bases=('directory.contactitem',),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('organization_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='directory.Organization')),
            ],
            options={
                'abstract': False,
            },
            bases=('directory.organization',),
        ),
        migrations.CreateModel(
            name='Museum',
            fields=[
                ('organization_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='directory.Organization')),
            ],
            options={
                'abstract': False,
            },
            bases=('directory.organization',),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('organization_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='directory.Organization')),
            ],
            options={
                'abstract': False,
            },
            bases=('directory.organization',),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('organization_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='directory.Organization')),
            ],
            options={
                'abstract': False,
            },
            bases=('directory.organization',),
        ),
    ]
