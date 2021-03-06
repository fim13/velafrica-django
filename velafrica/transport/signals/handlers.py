#-*- coding: utf-8 -*-
# Signals for sending automated mails
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.urls import reverse
from django.core.validators import validate_email
from django.db.models.signals import post_save
from django.dispatch import receiver

from velafrica.transport.models import Ride


@receiver(post_save, sender=Ride)
def send_email(sender, instance, created, **kwargs):
    """
    Send email notification to bicycle donor.
    """

    # check if the event has been newly created or just updated
    if not created:
        return

    warehouse = instance.to_warehouse

    # check if the warehouse exists
    if not warehouse:
        return

    emails = warehouse.notify_on_incoming_transport
    receiver_list = []

    if instance.spare_parts:
        if emails:
            for line in emails.splitlines():
                try:
                    validate_email(line)
                except ValidationError as e:
                    print("oops! no email {}".format(line))
                else:
                    print("hooray! email is valid, notify {}".format(line))
                    receiver_list += [line]
    if receiver:
        subject = u"Neue Ersatzteile in {}".format(warehouse)

        r = 'admin:{}_{}_change'.format(instance._meta.app_label, instance._meta.model_name)
        admin_url = "http://tracking.velafrica.ch{}".format(reverse(r, args=[instance.id]))

        msg = u"Eine neue Lieferung vom Transport ist soeben im Lager {} eingetroffen.\n\nDatum: {}\nFahrzeug: {}\nFahrer: {}\nHerkunft: {}\nBemerkungen: {}\n\nFahrt anschauen: {}".format(warehouse, instance.date, instance.car, instance.driver, instance.from_warehouse, instance.note, admin_url)
        from_name = getattr(settings, 'EMAIL_FROM_NAME', 'Velafrica Tracking')
        from_email = getattr(settings, 'EMAIL_FROM_EMAIL', 'tracking@velafrica.ch')
        sender = u"{} <{}>".format(from_name, from_email)
        send_mail(subject, msg, sender, receiver_list, fail_silently=False)
