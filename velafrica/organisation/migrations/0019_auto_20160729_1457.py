# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 12:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0018_auto_20160729_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalorganisation',
            name='city',
        ),
        migrations.RemoveField(
            model_name='historicalorganisation',
            name='plz',
        ),
        migrations.RemoveField(
            model_name='historicalorganisation',
            name='street',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='city',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='plz',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='street',
        ),
    ]