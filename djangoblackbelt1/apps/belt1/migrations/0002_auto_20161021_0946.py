# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 13:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start', models.CharField(max_length=255)),
                ('end', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='users',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='last_name',
            new_name='username',
        ),
        migrations.AddField(
            model_name='trips',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='belt1.Users'),
        ),
    ]
