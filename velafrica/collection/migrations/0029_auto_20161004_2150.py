# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-04 19:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0028_collectionevent_complete'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collectionevent',
            options={'ordering': ['date_start'], 'verbose_name': 'Sammelanlass', 'verbose_name_plural': 'Sammelanl\xe4sse'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['name'], 'verbose_name': 'Event'},
        ),
        migrations.AlterModelOptions(
            name='eventcategory',
            options={'ordering': ['-name'], 'verbose_name': 'Event Kategorie', 'verbose_name_plural': 'Event Kategorien'},
        ),
    ]