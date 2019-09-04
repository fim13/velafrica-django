# -*- coding: utf-8 -*-
import datetime
import os
import uuid

import qrcode
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from django_resized import ResizedImageField
from velafrica.core.storage import MyStorage
from velafrica.stock.models import Warehouse
from velafrica.velafrica_sud.models import Container

from django.db import models, connection
from .settings import BIKE_TYPES, BRAKE_TYPES, BIKE_SIZES


# fs = MyStorage()


def bike_images(instance, filename):
    return 'bike_img/{}_{}'\
        .format(
            instance.id,
            # datetime.datetime.now().strftime('%Y-%m-%d'),
            filename
        )


def next_a_plus_number():
    with connection.cursor() as cursor:
        cursor.execute("SELECT MAX(number) AS num FROM bikes_bike")
        m = cursor.fetchone()
        if m[0]:
            return m[0] + 1
    return 1


def bike_id():
    return datetime.datetime.now().strftime('%y') + "-" + uuid.uuid4().hex[:6].upper()


class Bike(models.Model):

    id = models.CharField(primary_key=True, unique=True, default=bike_id, max_length=255)
    plotable = [
            "number",
            "type",
            "brand",
            "bike_model",
            "gearing",
#            "crankset",
            "drivetrain",
            "type_of_brake",
            "brake",
            "colour",
            "size",
            "suspension",
            "rear_suspension",
            "extraordinary"
        ]

    number = models.IntegerField(unique=True, default=next_a_plus_number, editable=True, verbose_name=u"No.")

    # Basic
    type = models.CharField(choices=BIKE_TYPES, null=True, max_length=255, verbose_name=u"Type")
    date = models.DateField(default=datetime.date.today, verbose_name=u"Date")
    visa = models.CharField(max_length=255, blank=True, verbose_name=u"Visa")
    warehouse = models.ForeignKey(Warehouse, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=u"Warehouse")

    # A+
    a_plus = models.BooleanField(default=False, verbose_name=u"A+")

    # Details
    brand = models.CharField(max_length=255, default="", blank=True, verbose_name=u"Brand")
    bike_model = models.CharField(max_length=255, default="", blank=True, verbose_name=u"Model")
    gearing = models.CharField(max_length=255, default="", blank=True, verbose_name=u"Group of components")
    # crankset = models.CharField(max_length=255, default="", blank=True, verbose_name=u"Crankset")
    drivetrain = models.CharField(max_length=255, default="", blank=True, verbose_name=u"Drivetrain")
    type_of_brake = models.CharField(choices=BRAKE_TYPES, max_length=255, default="", blank=True, verbose_name=u"Type of Brake")
    brake = models.CharField(max_length=255, default="", blank=True, verbose_name=u"Brake")
    colour = models.CharField(max_length=255, default="", blank=True, verbose_name=u"Colour")
    size = models.CharField(max_length=255, default='', blank=True, verbose_name=u"Size") # choices=BIKE_SIZES,
    suspension = models.CharField(max_length=255, null=True, blank=True, verbose_name=u"Suspension")
    rear_suspension = models.CharField(max_length=255, null=True, blank=True, verbose_name=u"Rear Suspension")
    extraordinary = models.TextField(max_length=255, null=True, blank=True, verbose_name=u"Extraordinary")


    # Image(s)
    image = ResizedImageField(size=[1920, 1080], upload_to=bike_images, blank=True, null=True, verbose_name=u"Image")  # storage=fs

    # Shipping

    container = models.ForeignKey(Container, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=u"Container")

    # Metadata
    date_created = models.DateField(auto_now_add=True, null=True)
    date_modified = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.type)

    def get_url(self):
        return reverse("admin:bikes_bike_change", args=[self.pk])


# The following auto-delete files from filesystem when they are unneeded:
def delete_file(filename):
    if os.path.isfile(filename):
        folder = os.path.dirname(filename)
        os.remove(filename)
        try:
            os.rmdir(folder)
        except OSError:
            return


@receiver(models.signals.post_delete, sender=Bike)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.image:
        delete_file(instance.image.path)


@receiver(models.signals.pre_save, sender=Bike)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Bike.objects.get(pk=instance.pk).image
    except Bike.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if old_file.name:
            delete_file(old_file.path)

