# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-11 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velafrica_sud', '0040_auto_20160810_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalreport',
            name='currency_rate',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=10, verbose_name=b'W\xc3\xa4hrungskurs zu USD'),
        ),
        migrations.AlterField(
            model_name='report',
            name='currency_rate',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=10, verbose_name=b'W\xc3\xa4hrungskurs zu USD'),
        ),
    ]