# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-02 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0020_auto_20160729_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalorganisation',
            name='facebook',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name=b'Facebook Page (URL)'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='facebook',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name=b'Facebook Page (URL)'),
        ),
        migrations.AlterField(
            model_name='historicalorganisation',
            name='website',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name=b'Website (URL)'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='website',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name=b'Website (URL)'),
        ),
    ]