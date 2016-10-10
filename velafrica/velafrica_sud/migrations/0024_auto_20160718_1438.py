# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 12:38
from __future__ import unicode_literals

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('velafrica_sud', '0023_auto_20160718_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='economic_payment_types',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(b'cash', b'Cash Payment'), (b'installment', b'Installment'), (b'card', b'Payment with Credit/Debit Card'), (b'phone', b'Payment with Mobile Phone'), (b'microloan', b'Micro Loan (e.g. in cooperation with Micro Finance Institution)'), (b'other', b'Other')], max_length=20),
        ),
    ]
