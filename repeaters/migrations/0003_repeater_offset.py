# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repeaters', '0002_auto_20171031_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='repeater',
            name='offset',
            field=models.CharField(blank=True, max_length=32, verbose_name='Offset'),
        ),
    ]
