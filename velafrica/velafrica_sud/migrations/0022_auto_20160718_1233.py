# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velafrica_sud', '0021_auto_20160705_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='communityproject_notes',
            field=models.TextField(blank=True, null=True, verbose_name=b'Bemerkungen'),
        ),
        migrations.AddField(
            model_name='report',
            name='economic_notes',
            field=models.TextField(blank=True, null=True, verbose_name=b'Bemerkungen'),
        ),
        migrations.AddField(
            model_name='report',
            name='employment_notes',
            field=models.TextField(blank=True, null=True, verbose_name=b'Bemerkungen'),
        ),
        migrations.AddField(
            model_name='report',
            name='mobilityprogram_notes',
            field=models.TextField(blank=True, null=True, verbose_name=b'Bemerkungen'),
        ),
        migrations.AddField(
            model_name='report',
            name='vocational_notes',
            field=models.TextField(blank=True, null=True, verbose_name=b'Bemerkungen'),
        ),
        migrations.AlterField(
            model_name='report',
            name='communityproject_areas',
            field=models.CharField(blank=True, choices=[(b'0', b'Schooling / Education'), (b'1', b'Entrepreneuership'), (b'2', b'Evnironment / Environmental protection'), (b'3', b'Mobility'), (b'4', b"Women's empowerment"), (b'5', b"Children's empowerment"), (b'6', b'Sports activities'), (b'7', b'Other')], max_length=1, null=True, verbose_name=b'Feld der Gemeinschaftsarbeit'),
        ),
        migrations.AlterField(
            model_name='report',
            name='communityproject_people_benefitted',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Anzahl Personen die profitiert haben vom Gemeinschaftsprojekt'),
        ),
        migrations.AlterField(
            model_name='report',
            name='communityproject_reinvest_profit_total',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'In Gemeinschaftsprojekte re-investierter Betrag'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_bicycles_amount',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Anzahl verkaufte Fahrr\xc3\xa4der'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_bicycles_turnover',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Umsatz Fahrr\xc3\xa4der'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_category1_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Kategorie 1'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_category1_pricerange',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Preisrange Kategorie 1'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_category2_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Kategorie 2'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_category2_pricerange',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Preisrange Kategorie 2'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_category3_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Kategorie 3'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_category3_pricerange',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Preisrange Kategorie 3'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_category4_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Kategorie 4'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_category4_pricerange',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Preisrange Kategorie 4'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_category5_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Kategorie 5'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_category5_pricerange',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Preisrange Kategorie 5'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_category6_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Kategorie 6'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_category6_pricerange',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Preisrange Kategorie 6'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_category7_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Kategorie 7'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_category7_pricerange',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Preisrange Kategorie 7'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_category8_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Kategorie 8'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_category8_pricerange',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Preisrange Kategorie 8'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_services_amount',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Anzahl verkaufte Dienstleistungen'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_services_turnover',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Umsatz Dienstleistungen'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_spareparts_amount',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Anzahl verkaufte Ersatzteile'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_spareparts_turnover',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Umsatz Ersatzteile'),
        ),
        migrations.AlterField(
            model_name='report',
            name='economic_turnover_total',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Total Umsatz'),
        ),
        migrations.AlterField(
            model_name='report',
            name='employment_fulltime_men',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Angestellte Vollzeit M\xc3\xa4nner'),
        ),
        migrations.AlterField(
            model_name='report',
            name='employment_fulltime_women',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Angestellte Vollzeit Frauen'),
        ),
        migrations.AlterField(
            model_name='report',
            name='employment_internship_men',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Angestellte Internship M\xc3\xa4nner'),
        ),
        migrations.AlterField(
            model_name='report',
            name='employment_internship_women',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Angestellte Internship Frauen'),
        ),
        migrations.AlterField(
            model_name='report',
            name='employment_parttime_men',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Angestellte Teilzeit M\xc3\xa4nner'),
        ),
        migrations.AlterField(
            model_name='report',
            name='employment_parttime_women',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Angestellte Teilzeit Frauen'),
        ),
        migrations.AlterField(
            model_name='report',
            name='employment_trainee_men',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Angestellte Trainee M\xc3\xa4nner'),
        ),
        migrations.AlterField(
            model_name='report',
            name='employment_trainee_women',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Angestellte Trainee Frauen'),
        ),
        migrations.AlterField(
            model_name='report',
            name='employment_volunteer_men',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Angestellte Freiwillige M\xc3\xa4nner'),
        ),
        migrations.AlterField(
            model_name='report',
            name='employment_volunteer_women',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Angestellte Freiwillige Frauen'),
        ),
        migrations.AlterField(
            model_name='report',
            name='mobilityprogram_people_benefitted',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Number of people that benefitted from mobility programm'),
        ),
        migrations.AlterField(
            model_name='report',
            name='vocational_completed_boys',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Anzahl Jungen Ausbildungsprogramm abgeschlossen'),
        ),
        migrations.AlterField(
            model_name='report',
            name='vocational_completed_girls',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Anzahl M\xc3\xa4dchen Ausbildungsprogramm abgeschlossen'),
        ),
        migrations.AlterField(
            model_name='report',
            name='vocational_exstudents_employed',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Studenten vom letzten Jahr die jetzt angestellt sind'),
        ),
        migrations.AlterField(
            model_name='report',
            name='vocational_exstudents_selfemployed_link',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Studenten vom letzten Jahr die jetzt bei einem Partnerbetrieb angestellt sind'),
        ),
        migrations.AlterField(
            model_name='report',
            name='vocational_exstudents_selfemployed_new',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Studenten vom letzten Jahr die jetzt bei einem anderen Betrieb angestellt sind'),
        ),
        migrations.AlterField(
            model_name='report',
            name='vocational_program_boys',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Anzahl Jungen im Ausbildungsprogramm'),
        ),
        migrations.AlterField(
            model_name='report',
            name='vocational_program_duration',
            field=models.CharField(blank=True, choices=[(b'0', b'less than 3 months'), (b'1', b'6 - 12 months'), (b'2', b'12 - 18 months'), (b'3', b'18 - 24 months'), (b'4', b'more than 24 months')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='vocational_program_girls',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Anzahl M\xc3\xa4dchen im Ausbildungsprogramm'),
        ),
    ]
