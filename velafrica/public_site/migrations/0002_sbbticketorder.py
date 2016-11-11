# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-11 18:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0034_auto_20161101_1151'),
        ('public_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SbbTicketOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name=b'Vorname')),
                ('last_name', models.CharField(max_length=255, verbose_name=b'Nachname')),
                ('address', models.CharField(max_length=255, verbose_name=b'Strasse und Hausnummer')),
                ('zip', models.CharField(max_length=255, verbose_name=b'PLZ und Ort')),
                ('email', models.CharField(max_length=255, verbose_name=b'E-Mail')),
                ('phone', models.CharField(blank=True, max_length=255, verbose_name=b'Telefonnummer')),
                ('note', models.TextField(blank=True, verbose_name=b'Bemerkung')),
                ('dropoff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='collection.Dropoff')),
            ],
            options={
                'verbose_name': 'SBB Ticketbestellung',
                'verbose_name_plural': 'SBB Ticketbestellungen',
            },
        ),
    ]
