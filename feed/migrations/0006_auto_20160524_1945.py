# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 19:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_remove_comment_approved_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='study',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
