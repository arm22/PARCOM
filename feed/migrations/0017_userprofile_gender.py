# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 05:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0016_auto_20160530_0536'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[(b'M', b'Male'), (b'F', b'Female')], max_length=1, null=True),
        ),
    ]
