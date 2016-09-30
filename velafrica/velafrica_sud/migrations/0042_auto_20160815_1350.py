# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 11:50
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('velafrica_sud', '0041_auto_20160811_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalPartnerStaff',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name=b'Name des Angestellten')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('partner', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='velafrica_sud.PartnerSud')),
                ('role', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='velafrica_sud.Role')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical partner staff',
            },
        ),
        migrations.CreateModel(
            name='PartnerStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name=b'Name des Angestellten')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='velafrica_sud.PartnerSud', verbose_name=b'Arbeitgeber')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='velafrica_sud.Role', verbose_name=b'Rolle')),
            ],
        ),
        migrations.RenameModel(
            old_name='HistoricalStaff',
            new_name='HistoricalReportStaff',
        ),
        migrations.RenameModel(
            old_name='Staff',
            new_name='ReportStaff',
        ),
        migrations.AlterModelOptions(
            name='historicalreportstaff',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical report staff'},
        ),
    ]
