from rest_framework import serializers

from bucket.models import Bucket, BucketItem


class BucketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        fields = '__all__'


class BucketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        fields = '__all__'


class BucketItemInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = BucketItem
        fields = '__all__'


class BucketDetailSerializer(serializers.ModelSerializer):
    items = BucketItemInlineSerializer(many=True)

    class Meta:
        model = Bucket
        fields = '__all__'
