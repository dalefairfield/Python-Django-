# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 14:22
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('belt1', '0002_auto_20161021_0946'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='trips',
            managers=[
                ('tripManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
