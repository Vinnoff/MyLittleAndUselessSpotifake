# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 17:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Spotifake', '0006_auto_20180117_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='album_entertainers',
            new_name='entertainers',
        ),
    ]
