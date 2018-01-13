from rest_framework import generics

from device.models import Device
from device.serializers import (
    DeviceCreateUpdateSerializer,
    DeviceViewSerializer
)


class DeviceListView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    filter_fields = ('uid', 'status', 'product')
    search_fields = ('uid', 'product__name')
    ordering_fields = ('status', 'uid', 'product', 'product__name')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DeviceCreateUpdateSerializer
        return DeviceViewSerializer


class DeviceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DeviceViewSerializer
        return DeviceCreateUpdateSerializer
