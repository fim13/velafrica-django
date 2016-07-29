# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0026_auto_20160727_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproduct',
            name='purchase_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name=b'Verkaufspreis'),
        ),
        migrations.AddField(
            model_name='product',
            name='purchase_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name=b'Verkaufspreis'),
        ),
    ]