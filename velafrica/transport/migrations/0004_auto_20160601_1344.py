# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 11:44
from __future__ import unicode_literals

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0003_historicaldriver_historicalvelostate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalride',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Datum'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Datum'),
        ),
    ]
