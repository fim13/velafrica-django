# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0012_auto_20160613_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionevent',
            name='notes',
            field=models.TextField(blank=True, help_text=b'Weitere Infos / Bemerkungen', verbose_name=b'weitere Infos'),
        ),
    ]