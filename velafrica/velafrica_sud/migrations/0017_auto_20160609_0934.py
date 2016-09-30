# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 07:34
from __future__ import unicode_literals

import django_resized.forms
from django.db import migrations, models

import velafrica.core.ftp


class Migration(migrations.Migration):

    dependencies = [
        ('velafrica_sud', '0016_auto_20160608_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpartnersud',
            name='image',
            field=models.TextField(blank=True, help_text=b'Foto vom Partner vor Ort.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='partnersud',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, help_text=b'Foto vom Partner vor Ort.', null=True, storage=velafrica.core.ftp.MyFTPStorage(), upload_to=b'velafrica_sud/partner/'),
        ),
    ]
