# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-08 15:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_add_field_observations_to_check'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('hours', models.IntegerField(verbose_name='hours')),
                ('oil_type', models.CharField(blank=True, max_length=254, null=True, verbose_name='oil_type')),
                ('oil', models.BooleanField(default=False, verbose_name='oil')),
                ('oil_filter', models.BooleanField(default=False, verbose_name='oil_filter')),
                ('fuel_filter', models.BooleanField(default=False, verbose_name='fuel_filter')),
                ('air_filter', models.BooleanField(default=False, verbose_name='air_filter')),
                ('refrigerant', models.BooleanField(default=False, verbose_name='refrigerant')),
                ('battery', models.BooleanField(default=False, verbose_name='battery ')),
                ('observations', models.TextField(blank=True, null=True, verbose_name='observations')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'db_table': 'services',
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
    ]
