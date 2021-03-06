# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-10-26 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=20)),
                ('company_count', models.IntegerField()),
                ('company_address', models.CharField(max_length=30)),
                ('company_register', models.DateTimeField()),
            ],
            options={
                'db_table': 'company',
            },
        ),
    ]
