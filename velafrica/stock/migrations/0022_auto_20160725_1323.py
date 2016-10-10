# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 11:23
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0015_auto_20160725_0904'),
        ('stock', '0021_auto_20160725_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalpurchaseorder',
            old_name='to',
            new_name='from_org',
        ),
        migrations.RenameField(
            model_name='historicalsalesorder',
            old_name='to',
            new_name='from_org',
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='to',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='to',
        ),
        migrations.AddField(
            model_name='historicalpurchaseorder',
            name='to_org',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='organisation.Organisation'),
        ),
        migrations.AddField(
            model_name='historicalsalesorder',
            name='to_org',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='organisation.Organisation'),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='from_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchaseorder_from', to='organisation.Organisation'),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='to_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchaseorder_to', to='organisation.Organisation'),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='from_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salesorder_from', to='organisation.Organisation'),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='to_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salesorder_to', to='organisation.Organisation'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='from_org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_from', to='organisation.Organisation', verbose_name=b'Rechnungssteller'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='purchaseorder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.PurchaseOrder', verbose_name=b'Kaufauftrag (Purchase Order)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='salesorder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.SalesOrder', verbose_name=b'Kundenauftrag (Sales Order)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='to_org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_to', to='organisation.Organisation', verbose_name=b'Rechnungsempf\xc3\xa4nger'),
        ),
    ]
