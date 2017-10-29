from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from card.models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

    def validate_uid(self, value):
        exclude_id = self.instance.id if self.instance else 0
        value = value.strip()
        if Card.objects.filter(uid=value).exclude(id=exclude_id).exists():
            raise ValidationError("Card with provided UID already exists!")
        return value
