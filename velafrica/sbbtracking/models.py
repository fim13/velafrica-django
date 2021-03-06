# -*- coding: utf-8 -*-
from datetime import date
from django.conf import settings
from django.core.validators import EmailValidator
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django_resized import ResizedImageField
from simple_history.models import HistoricalRecords

from velafrica.core.storage import MyStorage
from velafrica.organisation.models import Organisation
from velafrica.velafrica_sud.models import Container

fs = MyStorage()

"""
class Donor(models.Model):
    first_name = models.CharField(blank=False, null=False, max_length=255, verbose_name="Vorname")
    last_name = models.CharField(blank=False, null=False, max_length=255, verbose_name="Nachname")
    email = models.CharField(blank=False, null=False, max_length=255, verbose_name="Email", validators=[EmailValidator])

    def __str__(self):
        return u"#{} {} <{}>".format(self.tracking_no, self.donor.first_name, self.donor.last_name, self.number_of_velos)
"""

class TrackingEventType(models.Model):
    """
    Tracking event types, recommended:

    1. Tracking erstellt
    2. Eingang Velafrica
        3a. Bereit für Export
            4. Containerverlad
            5. Ankunft Partner in Afrika
        3b. Zerlegung in Einzelteile
        3c. Verkauf


    """
    name = models.CharField(blank=False, null=False, max_length=255)
    show_partner_info = models.BooleanField(default=False, help_text="Zeige Partnerinfo an wenn vorhanden (Wird aus hinterlegtem Container ausgelesen).")
    description = models.TextField(blank=True, null=True)
    email_text = models.TextField(blank=True, null=True, help_text='Text der im Benachrichtigugsemail den den Spender geschickt wird.')
    image = ResizedImageField(storage=fs, size=[600, 600], upload_to='tracking/eventtypes/', blank=True, null=True, verbose_name="Symbolbild")
    label = models.CharField(blank=True, null=True, max_length=255, verbose_name="Label", help_text="Text Label auf der Tracking Seite (optional)")
    required_previous_event = models.ForeignKey(
        'TrackingEventType',
        blank=True,
        null=True,
        verbose_name="Vorangehender Event",
        help_text="Wird dieses Feld ausgefüllt, muss der letzte Event auf dem Tracking vom angegebenen Typ sein, sonst kann kein Event dieses Event Typs hinzugefügt werden. Dies soll verhindern dass Events vergessen gehen.",
        on_delete=models.SET_NULL)
    arrival_africa = models.BooleanField(
        blank=False,
        null=False,
        default=False,
        verbose_name="Steht für Ankunft in Afrika",
        help_text="Wird diese Option aktiviert, wird dieser Event Typ verwendet beim Container verbuchen um verlinkte Trackings zu markieren"
        )    
    complete_tracking = models.BooleanField(
        blank=False,
        null=False,
        default=False,
        verbose_name="Schliesst Tracking ab?",
        help_text="Gilt ein Tracking mit diesem Event als beendet?"
    )
    send_email = models.BooleanField(
        blank=False, 
        null=False, 
        help_text="Aktivieren falls bei Erstellung eines Events dieser Art automatisch ein Email an den Spender versandt werden soll."
    )
    latitude_default = models.DecimalField(blank=True, null=True, verbose_name='Breitengrad Standard', max_digits=9, decimal_places=6)
    longitude_default = models.DecimalField(blank=True, null=True, verbose_name='Längengrad Standard', max_digits=9, decimal_places=6)

    history = HistoricalRecords()

    def next_tracking_eventtype_options(self):
        """
        Returns a list of the tracking event types that can be added next
        """
        return TrackingEventType.objects.filter(required_previous_event=self.event_type)

    def __str__(self):
        return u"{}".format(self.name)

    class Meta:
        ordering = ['name']


class TrackingEvent(models.Model):
    """
    Represents an event during tracking of a bicycle.
    """
    datetime = models.DateTimeField(blank=False, null=False, default=timezone.now, verbose_name="Zeitpunkt")
    event_type = models.ForeignKey(TrackingEventType, help_text="Art des Events", on_delete=models.CASCADE)
    tracking = models.ForeignKey('Tracking', on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organisation, null=True, blank=True, verbose_name="Organisation", help_text="Organisation welche den Event erstellt hat.", on_delete=models.CASCADE)
    latitude = models.DecimalField(blank=True, null=True, verbose_name='Breitengrad', max_digits=9, decimal_places=6)
    longitude = models.DecimalField(blank=True, null=True, verbose_name='Längengrad', max_digits=9, decimal_places=6)
    note = models.CharField(blank=True, null=True, max_length=255, verbose_name="Bemerkung", help_text="interne Bemerkung, nirgends ersichtlich für Spender (optional)")
    history = HistoricalRecords()

    def __str__(self):
        return u"{}".format(self.event_type.name)

    def get_description(self):
        """
        Get the description to display.
        """
        description = u"{}".format(self.event_type.description)
        if self.event_type.show_partner_info and self.tracking.container:
            partner = self.tracking.container.partner_to
            if partner.get_description():
                description += u"\n<h3>{}</h3>{}\n<a href='{}' target='blank'>{}</a>".format(partner.get_name(), partner.get_description(), partner.get_website(), partner.get_website())
        return description

    def get_image(self):
        """
        Get the image to display together with the description.
        """
        if self.event_type.show_partner_info and self.tracking.container:
            print("almost return partner image")
            if self.tracking.container.partner_to.image:
                print("return partner image")
                return self.tracking.container.partner_to.image
        print("return event type image")
        return self.event_type.image

    class Meta:
        ordering = ['-datetime']
        unique_together = ['event_type', 'tracking']


class VeloType(models.Model):
    """
    Represents a type of bicycle.
    """
    name = models.CharField(blank=False, null=False, max_length=255, verbose_name="Bezeichnung")
    history = HistoricalRecords()

    def __str__(self):
        return u"{}".format(self.name)

def get_last_event(self, tracking_id):
        """
        Get the latest event dynamically.
        """
        return TrackingEvent.objects.filter(tracking=tracking_id).first()


class Tracking(models.Model):
    """
    Represents one bicycle that is being tracked.
    Last_event is a link to the last event that has been added on the tracking, it is representing the last known status.
    Via the last_event, one can also find out where (last_event.organisation) the bicycle has been scanned the last time.
    """
    tracking_no = models.CharField(blank=False, null=False, max_length=50, unique=True, verbose_name="Tracking Nummer")
    vpn = models.ForeignKey(Organisation, 
        null=True, 
        blank=True, 
        verbose_name="Partner", 
        help_text="wird momentan noch nicht berücksichtigt", on_delete=models.CASCADE
    )

    #donor = models.ForeignKey(Person, on_delete=models.SET_NULL)

    first_name = models.CharField(blank=True, null=True, max_length=255, verbose_name="Vorname")
    last_name = models.CharField(blank=True, null=True, max_length=255, verbose_name="Nachname")
    email = models.CharField(blank=True, null=True, max_length=255, verbose_name="Email", validators=[EmailValidator])
    container = models.ForeignKey(Container, blank=True, null=True, on_delete=models.SET_NULL)
    note = models.CharField(blank=True, null=True, max_length=255, verbose_name="Bemerkung")
    velo_type = models.ForeignKey('VeloType', blank=True, null=True, on_delete=models.SET_NULL)
    last_event = models.ForeignKey(
        'TrackingEvent',
        null=True, 
        blank=True,
        verbose_name='Letzter Event',
        related_name='tracking_last_event',
        on_delete=models.SET_NULL)
    complete = models.BooleanField(default=False, verbose_name='Abgeschlossen')

    history = HistoricalRecords()

    def check_completion(self):
        """
        Manually check if tracking is complete.
        """
        last = self.get_last_event()
        if last:
            if last.complete_tracking:
                self.complete = True
                self.save()
                return True
        return False

    def set_last_event(self):
        """
        Set last event manually.
        """
        event = TrackingEvent.objects.filter(tracking=self.id).first()
        if event:
            # check if is already set correctly to save performance
            if event != self.last_event:
                self.last_event = event
                self.save()
            return event
        else:
            return None

    def get_last_event(self):
        """
        Get the latest event dynamically.
        """
        return self.set_last_event()
    get_last_event.short_description = 'Last event'

    def get_last_update(self):
        """
        Get last update manually.
        """
        event = self.get_last_event()
        if event:
            return event.datetime
        else:
            return None
    get_last_update.short_description = 'Last event'


    def add_event(self, t_event_type):
        """
        Add :model:`sbbtracking.TrackingEvent` to :model:`sbbtracking.Tracking` 

        Checks if event requirements are met.
        """
        if not t_event_type:
            print("t_event_type not defined")
            return False

        # first off, set last event to be sure it is correct
        last_event = self.set_last_event()
        if last_event:
            if last_event.event_type == t_event_type.required_previous_event:
                te = TrackingEvent(event_type=t_event_type, tracking=self)
                te.save()
                return True
            else:
                print("Sorry, last event was not {}, but {}".format(t_event_type.required_previous_event, last_event.event_type))
                return False
        return None

    def __str__(self):
        return u"#{}: {} {}".format(self.tracking_no, self.first_name, self.last_name)

    def next_tracking_eventtype_options(self):
        """
        Returns a list of :model:`sbbtracking.TrackingEventType` that can be added next.
        """
        
        # first off, set last event to be sure it is correct
        last_event = self.set_last_event()
        if last_event:
            return TrackingEventType.objects.filter(required_previous_event=last_event.event_type)
        else:
            return TrackingEventType.objects.filter(required_previous_event=None)

    @staticmethod
    def get_tracked_velo_count(this_year = False, without_initial = False):
        inital_velo = getattr(settings, 'INITIAL_VELO_COUNT', 0)
        average_per_day = getattr(settings, 'AVERAGE_VELOS_PER_DAY', 0)
        days = (date.today() - date(2017, 1, 1)).days

        # this only applies when the function is called before 1.1.2017 (to prevent calculation with negative numbers
        if days < 0:
            days *= -1

        # TODO: make this more dynamic, as the event ids could be different
        # (4 = Containerverlad, 5 = Ankunft Partner Afrika)
        if this_year:
            trackings = Tracking.objects.filter(Q(Q(Q(last_event__event_type_id=4) | Q(last_event__event_type_id=5))) & Q(last_event__datetime__year=date.today().year)).count()
        else:
            trackings = Tracking.objects.filter(Q(Q(last_event__event_type_id=4) | Q(last_event__event_type_id=5))).count()
        return inital_velo + days * average_per_day + trackings if not without_initial else days * average_per_day + trackings

    class Meta:
        ordering = ['-tracking_no']


class EmailLog(models.Model):
    """
    Helper class, used to log sent emails.
    """
    tracking = models.ForeignKey(Tracking, on_delete=models.CASCADE)
    tracking_event = models.ForeignKey(TrackingEvent, on_delete=models.CASCADE)
    subject = models.CharField(blank=False, null=False, max_length=255)
    sender = models.CharField(blank=False, null=False, max_length=255)
    receiver = models.CharField(blank=False, null=False, max_length=255)
    datetime = models.DateTimeField(blank=False, null=False, default=timezone.now)
    message = models.TextField(blank=True, null=True)
    history = HistoricalRecords()
