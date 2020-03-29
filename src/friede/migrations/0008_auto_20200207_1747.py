# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2020-02-07 17:47
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friede', '0007_auto_20200202_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='ops',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(default=dict), blank=True, default=list, null=True, size=None),
        ),
    ]