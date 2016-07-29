# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 12:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organisation', '0015_auto_20160725_0904'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0025_auto_20160727_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalInvoice',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('comments', models.TextField(blank=True, null=True, verbose_name=b'Kommentare')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('from_org', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='organisation.Organisation')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical invoice',
            },
        ),
        migrations.CreateModel(
            name='HistoricalPurchaseOrder',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('comments', models.TextField(blank=True, null=True, verbose_name=b'Kommentare')),
                ('state', models.CharField(choices=[(b'3', b'invoiced'), (b'2', b'shipped'), (b'4', b'complete'), (b'0', b'draft'), (b'1', b'confirmed')], default=b'0', max_length=2, verbose_name=b'Status')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('from_org', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='organisation.Organisation')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('to_org', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='organisation.Organisation')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical purchase order',
            },
        ),
        migrations.CreateModel(
            name='HistoricalSalesOrder',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('comments', models.TextField(blank=True, null=True, verbose_name=b'Kommentare')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('from_org', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='organisation.Organisation')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('to_org', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='organisation.Organisation')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical sales order',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True, null=True, verbose_name=b'Kommentare')),
                ('from_org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_from', to='organisation.Organisation', verbose_name=b'Rechnungssteller')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceListPos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0, verbose_name=b'St\xc3\xbcckzahl')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commission.Invoice')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_on', models.DateField(default=django.utils.timezone.now, verbose_name=b'Eingangsdatum')),
                ('amount', models.IntegerField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commission.Invoice')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True, null=True, verbose_name=b'Kommentare')),
                ('state', models.CharField(choices=[(b'3', b'invoiced'), (b'2', b'shipped'), (b'4', b'complete'), (b'0', b'draft'), (b'1', b'confirmed')], default=b'0', max_length=2, verbose_name=b'Status')),
                ('from_org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchaseorder_from', to='organisation.Organisation')),
                ('to_org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchaseorder_to', to='organisation.Organisation')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrderListPos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0, verbose_name=b'St\xc3\xbcckzahl')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Product')),
                ('purchaseorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commission.PurchaseOrder')),
            ],
        ),
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True, null=True, verbose_name=b'Kommentare')),
                ('from_org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salesorder_from', to='organisation.Organisation')),
                ('to_org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salesorder_to', to='organisation.Organisation')),
            ],
        ),
        migrations.CreateModel(
            name='SalesOrderListPos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0, verbose_name=b'St\xc3\xbcckzahl')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Product')),
                ('salesorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commission.SalesOrder')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='purchaseorder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commission.PurchaseOrder', verbose_name=b'Kaufauftrag (Purchase Order)'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='salesorder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commission.SalesOrder', verbose_name=b'Kundenauftrag (Sales Order)'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='to_org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_to', to='organisation.Organisation', verbose_name=b'Rechnungsempf\xc3\xa4nger'),
        ),
        migrations.AddField(
            model_name='historicalinvoice',
            name='purchaseorder',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='commission.PurchaseOrder'),
        ),
        migrations.AddField(
            model_name='historicalinvoice',
            name='salesorder',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='commission.SalesOrder'),
        ),
        migrations.AddField(
            model_name='historicalinvoice',
            name='to_org',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='organisation.Organisation'),
        ),
        migrations.AlterUniqueTogether(
            name='salesorderlistpos',
            unique_together=set([('salesorder', 'product')]),
        ),
        migrations.AlterUniqueTogether(
            name='purchaseorderlistpos',
            unique_together=set([('purchaseorder', 'product')]),
        ),
        migrations.AlterUniqueTogether(
            name='invoicelistpos',
            unique_together=set([('invoice', 'product')]),
        ),
    ]