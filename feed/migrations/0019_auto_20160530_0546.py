# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 05:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0018_auto_20160530_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(choices=[(b'M', b'Male'), (b'F', b'Female'), (b'NA', b'Not Applicable')], max_length=1, null=True),
        ),
    ]
