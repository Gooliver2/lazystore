from rest_framework import serializers

from card.models import Card


class CardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class CardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class CardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'
