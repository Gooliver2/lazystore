from django.db import models


class ProductType(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="product_types")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name="product name", max_length=255)
    description = models.TextField(verbose_name="product description", blank=True, null=True)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to="products")

    type = models.ForeignKey('ProductType', related_name="products")

    def __str__(self):
        return self.name

