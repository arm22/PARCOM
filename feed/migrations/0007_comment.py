# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 19:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_auto_20160524_1945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='feed.Study')),
            ],
        ),
    ]
