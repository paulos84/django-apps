# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 03:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annual', '0008_auto_20170202_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyMean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('pollutant', models.CharField(max_length=10)),
                ('concentration', models.FloatField(max_length=10)),
            ],
        ),
    ]
