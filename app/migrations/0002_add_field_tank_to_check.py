# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-05 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_create_model_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='tank',
            field=models.FloatField(default=0, verbose_name='tank'),
            preserve_default=False,
        ),
    ]
