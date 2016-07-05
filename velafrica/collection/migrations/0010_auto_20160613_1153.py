# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 09:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0009_auto_20160613_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.EventCategory', verbose_name=b'Kategorie'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name=b'Beschreibung'),
        ),
        migrations.AlterField(
            model_name='event',
            name='host',
            field=models.CharField(max_length=255, verbose_name=b'Veranstalter'),
        ),
        migrations.AlterField(
            model_name='taskprogress',
            name='notes',
            field=models.TextField(blank=True, verbose_name=b'Notizen'),
        ),
        migrations.AlterField(
            model_name='taskprogress',
            name='status',
            field=models.BooleanField(default=False, verbose_name=b'Erledigt?'),
        ),
    ]