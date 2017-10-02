from django.db import models

from card.models import Card
from product.models import Product


class Bucket(models.Model):
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'

    STATUS_CHOICES = (
        (IN_PROGRESS, 'Bucket is not finished yet'),
        (COMPLETED, 'Bucket completed with transaction'),
    )

    status = models.CharField(choices=STATUS_CHOICES, default=IN_PROGRESS, max_length=11)
    card = models.ForeignKey(Card, related_name="buckets")

    def __str__(self):
        return "%s __ in __ %s" % (self.card, self.get_status_display())


class BucketItem(models.Model):
    bucket = models.ForeignKey('Bucket', related_name="items")
    product = models.ForeignKey(Product, related_name="bucket_items", null=True, blank=True)
    product_name = models.CharField(verbose_name="product name", max_length=255)

    amount = models.FloatField(default=0, verbose_name="Amount of product", help_text="(weight, pieces, etc.)")
    price = models.FloatField(default=0, verbose_name="Total product price")

    def __str__(self):
        return "%s - %s - %s - %s" % (self.bucket_id,self.product_name, self.amount, self.price)
