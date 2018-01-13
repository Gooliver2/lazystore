from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from device.models import Device


class DeviceViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
        depth = 1


class DeviceCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

    def validate_uid(self, value):
        exclude_id = self.instance.id if self.instance else 0
        value = value.strip()
        if Device.objects.filter(uid=value).exclude(id=exclude_id).exists():
            raise ValidationError("Card with provided UID already exists!")
        return value

    def update(self, instance, validated_data):
        instance = super(DeviceCreateUpdateSerializer, self).update(instance, validated_data)
        self._data = DeviceViewSerializer(instance=instance).data
        return instance
