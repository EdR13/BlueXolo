# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-13 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20171011_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_info',
            field=models.TextField(blank=True),
        ),
    ]
