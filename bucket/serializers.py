from rest_framework import serializers

from bucket.models import Bucket, BucketItem


class BucketItemInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = BucketItem
        fields = '__all__'


class BucketSerializer(serializers.ModelSerializer):
    items = BucketItemInlineSerializer(many=True, read_only=True)

    class Meta:
        model = Bucket
        field = ['items']
        fields = '__all__'

    def create(self, validated_data):
        instance = super(BucketSerializer, self).create(validated_data)

        for item_data in self.initial_data.get('items', []):
            item_data.update(bucket=instance.id)
            item_serializer = BucketItemInlineSerializer(data=item_data)
            if item_serializer.is_valid(raise_exception=True):
                item_serializer.save()

        return instance

    def update(self, instance, validated_data):
        instance.items.all().delete()

        for item_data in self.initial_data.get('items', []):
            item_data.update(bucket=instance.id)
            item_serializer = BucketItemInlineSerializer(data=item_data)
            if item_serializer.is_valid(raise_exception=True):
                item_serializer.save()

        return instance
