# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-06-27 15:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aries', '0004_auto_20190621_0131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('version', models.CharField(default='0.0.0', max_length=32)),
                ('available', models.CharField(default='0.0.0', max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='group',
            name='permissions',
        ),
        migrations.AddField(
            model_name='group',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='group',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='policy',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='role',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='auth_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='aries_data', serialize=False, to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='auth_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='aries_data', serialize=False, to='auth.Permission'),
        ),
    ]