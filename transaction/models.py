from django.db import models

from bucket.models import Bucket


class Transaction(models.Model):
    CREDIT = 'credit'
    CASH = 'cash'

    PAYMENT_TYPE_CHOICES = (
        (CREDIT, 'Credit card'),
        (CASH, 'CASH'),
    )

    bucket = models.OneToOneField(Bucket, related_name="transaction")
    payment_type = models.CharField(choices=PAYMENT_TYPE_CHOICES, default=CASH, max_length=10)
    sum = models.FloatField(verbose_name="total sum in receipt", default=0)
    cash = models.FloatField(verbose_name="money amount, payed by buyer", default=0)
    change = models.FloatField(verbose_name="change from cash", default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s - %s" % (self.bucket, self.get_payment_type_display(), self.sum)
