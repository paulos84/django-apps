# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 14:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annual', '0012_auto_20170205_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailymean',
            name='Date',
        ),
    ]