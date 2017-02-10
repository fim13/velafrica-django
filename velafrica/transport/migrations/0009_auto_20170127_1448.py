# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-27 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0008_auto_20160811_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalride',
            name='to_warehouse_detail_address',
            field=models.TextField(blank=True, help_text=b'Bei Auswahl von "Diverse Spender" als Ziel, kann hier optional die genaue Adresse eingetragen werden.', null=True, verbose_name=b'TO_WAREHOUSE alternative Adress (optional)'),
        ),
        migrations.AddField(
            model_name='ride',
            name='to_warehouse_detail_address',
            field=models.TextField(blank=True, help_text=b'Bei Auswahl von "Diverse Spender" als Ziel, kann hier optional die genaue Adresse eingetragen werden.', null=True, verbose_name=b'TO_WAREHOUSE alternative Adress (optional)'),
        ),
    ]