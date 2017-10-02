from django.contrib import admin

from bucket.models import Bucket, BucketItem

admin.site.register(Bucket)
admin.site.register(BucketItem)
