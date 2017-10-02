from rest_framework import generics

from device.models import Device
from device.serializers import (
    DeviceListSerializer,
    DeviceCreateSerializer,
    DeviceDetailSerializer
)


class DeviceListView(generics.ListCreateAPIView):
    queryset = Device.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DeviceCreateSerializer
        return DeviceListSerializer


class DeviceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceDetailSerializer
