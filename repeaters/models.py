from django.db import models
from core.models import TimeStampedModel


class Repeater(TimeStampedModel):
    """Repeater Model"""

    callsign = models.CharField('Repeater Callsign', max_length=128)
    input_frequency = models.CharField('Input Frequency', max_length=128, default='144.000')
    output_frequency = models.CharField('Output Frequency', max_length=128, blank=True)
    offset = models.CharField('Offset', max_length=32, blank=True)
    is_active = models.BooleanField('Is Active', default=False)

    def __str__(self):
        return "Repeater {0} - {1} MHZ".format(self.callsign, self.output_frequency)

    class Meta:
        ordering = ['callsign']


class RepeaterLocation(TimeStampedModel):
    """Repeater Location Model"""

    repeater = models.ForeignKey(
        'Repeater',
        Repeater,
        related_name="locations",
        related_query_name="location",
    )
    longitude = models.CharField('Longitude', blank=True, max_length=64)
    latitude = models.CharField('Latitude', blank=True, max_length=64)
    address = models.CharField('Address', blank=True, max_length=255)
    city = models.CharField('City', blank=True, max_length=128)
    state = models.CharField('State', blank=True, max_length=2)
    postal_code = models.CharField('Postal Code', blank=True, max_length=255)

    def __str__(self):
        return "Location {0} - {1}".format(self.longitude, self.latitude)


class RepeaterDigitalModes(TimeStampedModel):
    repeater = models.ForeignKey(
        'Repeater',
        Repeater,
        related_name="digitalmodes",
        related_query_name="digitalmode",
    )
    c4fm = models.BooleanField('C4FM', blank=True, default=False)
    d_star = models.BooleanField('D-STAR', blank=True, default=False)
    dmr = models.BooleanField('DMR', blank=True, default=False)


class RepeaterLinkModes(TimeStampedModel):
    repeater = models.ForeignKey(
        'Repeater',
        Repeater,
        related_name="linkmodes",
        related_query_name="linkmode",
    )
    echolink = models.BooleanField('EchoLink', blank=True, default=False)
    irlp = models.BooleanField('IRLP', blank=True, default=False)



