# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0008_auto_20160610_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='municipality',
            name='id',
        ),
        migrations.AlterField(
            model_name='municipality',
            name='gdenr',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name=b'Gemeindenr. des BFS'),
        ),
    ]