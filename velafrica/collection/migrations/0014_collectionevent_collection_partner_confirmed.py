# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0013_auto_20160613_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectionevent',
            name='collection_partner_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]