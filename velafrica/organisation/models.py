# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from simple_history.models import HistoricalRecords

from velafrica.core import utils


class Country(models.Model):
    """
    Represents a country of the world.
    """
    name = models.CharField(blank=False, null=False, max_length=255, verbose_name="Name des Landes", unique=True)
    code = models.CharField(blank=True, null=True, max_length=255, verbose_name=u"Ländercode (ISO 3166-1 alpha-2)",
                            unique=True)

    def __str__(self):
        return u"{}".format(self.name)

    class Meta:
        ordering = ['-name']
        verbose_name_plural = "Countries"


class Address(models.Model):
    """
    Represents the address of an organisation / partner / warehouse.

    :model:`organisation.Country`
    """
    street = models.CharField(blank=True, null=True, max_length=255, verbose_name="Strasse und Hausnummer")
    zipcode = models.IntegerField(blank=True, null=True, verbose_name="Zipcode / PLZ")
    city = models.CharField(blank=True, null=True, max_length=255, verbose_name="Ort")
    state = models.CharField(blank=True, null=True, max_length=255, verbose_name="Kanton / Region")
    country = models.ForeignKey(Country, verbose_name="Land", on_delete=models.CASCADE)

    latitude = models.DecimalField(blank=True, null=True, verbose_name='Breitengrad', max_digits=9, decimal_places=6)
    longitude = models.DecimalField(blank=True, null=True, verbose_name='Längengrad', max_digits=9, decimal_places=6)

    def get_geolocation(self):
        """
        """
        # first check if at least city and country are provided, otherwise don't get geolocation
        if self.city and self.country:
            loc = utils.get_geolocation(self.__str__())
            if loc:
                self.latitude = loc['lat']
                self.longitude = loc['lng']
                self.save()
                return loc
        return None

    def get_googlemaps_url(self):
        """
        """
        # address should at least have country and city provided, everything else is to inacurate
        if self.country and self.city:
            return u"{}".format(utils.get_googlemaps_url_place(self.__str__()))
        return None

    def __str__(self):
        __str = u""
        if self.street:
            __str += u"{}".format(self.street)
        if self.zipcode:
            if len(__str) > 0:
                __str += u", "
            __str += u"{}".format(self.zipcode)
        if self.city:
            if len(__str) > 0:
                if not self.zipcode:
                    __str += u", "
                else:
                    __str += u" "
            __str += u"{}".format(self.city)
        if self.country:
            if len(__str) > 0:
                __str += u", "
            __str += u"{}".format(self.country)
        return __str

    class Meta:
        verbose_name_plural = "Addresses"


class Organisation(models.Model):
    """
    Represents a network partner.
    
    Both Swiss and African partners are represented as organisations.

    African partners do have a linked :model:`velafrica_sud.PartnerSud` instance.
    """

    name = models.CharField(blank=False, null=True, max_length=255, verbose_name="Name der Organisation")
    website = models.URLField(blank=True, null=True, max_length=255, verbose_name="Website (URL)")
    facebook = models.URLField(blank=True, null=True, max_length=255, verbose_name="Facebook Page (URL)")
    address = models.ForeignKey(Address, verbose_name="Adresse", blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True, null=True)
    contact = models.TextField(verbose_name="Info Kontakt", blank=True,
                               null=True)
    contact_person = models.CharField(blank=True, default="", max_length=255, verbose_name="Kontaktperson")
    phone = models.CharField(blank=True, default="", max_length=255, verbose_name="Tel Nr.")
    email = models.CharField(blank=True, default="", max_length=255, verbose_name="E-Mail")

    history = HistoricalRecords()

    def is_partnersud(self):
        """
        """
        if self.partnersud:
            return True
        else:
            return False

    is_partnersud.short_description = "Süd Partner"

    def get_partnersud(self):
        """
        """
        if self.partnersud:
            return self.partnersud
        else:
            return "-"

    get_partnersud.short_description = "Süd Partner"

    def __str__(self):
        if self.address and self.address.city:
            return u"{}, {}".format(self.name, self.address.city)
        else:
            return u"{}".format(self.name)

    class Meta:
        ordering = ['name']


class Person(models.Model):
    """
    Person working at a network partner.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Django User Account"
    )
    organisation = models.ForeignKey('Organisation', verbose_name="Arbeitgeber", on_delete=models.CASCADE)

    def __str__(self):
        if (len(self.user.first_name) > 0 and len(self.user.last_name) > 0):
            return u"{} {} ({})".format(self.user.first_name, self.user.last_name, self.organisation.name)
        else:
            return u"{} ({})".format(self.user.username, self.organisation.name)

    class Meta:
        verbose_name_plural = "People"
