from django.db import models


class Card(models.Model):
    ACTIVE = 'active'
    INACTIVE = 'inactive'

    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Active')
    )

    uid = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS_CHOICES, default=INACTIVE, max_length=10)

    def __str__(self):
        return "%s - %s" % (self.uid, self.status)
