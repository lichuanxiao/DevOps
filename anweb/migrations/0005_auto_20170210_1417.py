# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anweb', '0004_auto_20170210_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysql',
            name='extend',
            field=models.CharField(default='', max_length=100),
        ),
    ]