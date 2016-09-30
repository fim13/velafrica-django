# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 09:07
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_auto_20160601_1344'),
        ('transport', '0004_auto_20160601_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalride',
            name='stocklist',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='stock.StockList'),
        ),
        migrations.AddField(
            model_name='ride',
            name='stocklist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.StockList'),
        ),
    ]
