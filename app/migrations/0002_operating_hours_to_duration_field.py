# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-07 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_create_model_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='operating_hours',
            field=models.DurationField(verbose_name='operating_hours'),
        ),
    ]
