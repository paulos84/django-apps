# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 13:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annual', '0017_dailymean_pollurl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailymean',
            old_name='pollurl',
            new_name='poll',
        ),
    ]
