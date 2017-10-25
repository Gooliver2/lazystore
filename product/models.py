import os

from django.db import models
from django.template.defaultfilters import slugify


def product_type_filename(instance, filename):
    path = "product_types/"
    filename, ext = os.path.splitext(filename)
    filename = slugify(filename) + ext
    return os.path.join(path, filename)


def product_filename(instance, filename):
    path = "products/"
    filename, ext = os.path.splitext(filename)
    filename = slugify(filename) + ext
    return os.path.join(path, filename)


class ProductType(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=product_type_filename)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name="product name", max_length=255)
    description = models.TextField(verbose_name="product description", blank=True, null=True)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to=product_filename)

    type = models.ForeignKey('ProductType', related_name="products")

    def __str__(self):
        return self.name

