# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0019_auto_20160729_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Ort'),
        ),
    ]