# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 16:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
