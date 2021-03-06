# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 11:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt1', '0003_auto_20161021_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Joins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('trip_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='belt1.Trips')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='belt1.Users')),
            ],
        ),
    ]
