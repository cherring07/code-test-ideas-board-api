# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-07 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]