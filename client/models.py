from django.db import models

from device.models import Device


class Client(models.Model):
    KASSA = 'kassa'
    SCALES = 'scales'
    TYPE_CHOICES = (
        (KASSA, 'KASSA (Administrator application, used at checkout)'),
        (SCALES, 'SCALES (Application, used on each scales)')
    )

    type = models.CharField(max_length=6, choices=TYPE_CHOICES, default=SCALES)
    device = models.ForeignKey(Device, related_name="client", null=True, blank=True)

    def __str__(self):
        return "%s - %s" % (self.get_type_display(), self.device)
