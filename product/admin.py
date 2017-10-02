from django.contrib import admin

from product.models import ProductType, Product

admin.site.register(ProductType)
admin.site.register(Product)
