# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-24 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_site', '0015_auto_20161123_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='sorting',
            field=models.IntegerField(default=0, verbose_name=b'Sortierung'),
        ),
    ]