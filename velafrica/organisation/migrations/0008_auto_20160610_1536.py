# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0007_auto_20160610_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='municipality',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='municipality',
            name='gdenr',
            field=models.IntegerField(unique=True, verbose_name=b'Gemeindenr. des BFS'),
        ),
    ]