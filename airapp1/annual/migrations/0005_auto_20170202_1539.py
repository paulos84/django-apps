# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 08:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annual', '0004_annualmean_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annualmean',
            old_name='url',
            new_name='slug',
        ),
    ]
