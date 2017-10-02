from rest_framework import serializers

from device.models import Device


class DeviceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
        depth = 1


class DeviceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class DeviceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
        depth = 1
