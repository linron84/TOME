# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 18:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0013_auto_20170605_1508'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='yeartopicrank',
            options={'ordering': ('year', '-score')},
        ),
    ]
