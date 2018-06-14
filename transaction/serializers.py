from rest_framework import serializers

from bucket.models import Bucket
from transaction.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        depth = 1


class TransactionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.bucket.status = Bucket.COMPLETED
        instance.bucket.save()
        return instance

