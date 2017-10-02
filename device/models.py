from django.db import models

from product.models import ProductType


class Device(models.Model):
    ACTIVE = 'active'
    INACTIVE = 'inactive'

    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Active')
    )

    uid = models.CharField(verbose_name="Device UID", max_length=255)
    status = models.CharField(choices=STATUS_CHOICES, default=INACTIVE, max_length=10)

    last_ping = models.DateTimeField(verbose_name="last keep_alive signal", null=True, blank=True)

    product_type = models.ForeignKey(ProductType, related_name="devices", null=True, blank=True)

    def __str__(self):
        return "%s - %s - for - %s" % (self.uid, self.get_status_display(), self.product_type)
