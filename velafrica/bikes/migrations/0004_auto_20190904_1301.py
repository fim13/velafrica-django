# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-09-04 11:01
from __future__ import unicode_literals

from django.db import migrations, models
import django_resized.forms
import velafrica.bikes.models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0003_auto_20190904_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='extraordinary',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Extraordinary'),
        ),
        migrations.AlterField(
            model_name='bike',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=75, size=[1920, 1080], upload_to=velafrica.bikes.models.bike_images, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='bike',
            name='size',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Size'),
        ),
    ]
