# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annual', '0003_annualmean_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='annualmean',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]