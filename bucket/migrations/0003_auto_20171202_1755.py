# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-02 17:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bucket', '0002_auto_20171002_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucket',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bucket',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]