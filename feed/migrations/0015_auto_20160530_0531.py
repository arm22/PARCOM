# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0014_auto_20160530_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
