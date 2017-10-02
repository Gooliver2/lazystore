from rest_framework import generics

from bucket.models import Bucket
from bucket.serializers import BucketDetailSerializer, BucketListSerializer, BucketCreateSerializer


class BucketListView(generics.ListCreateAPIView):
    queryset = Bucket.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BucketCreateSerializer
        return BucketListSerializer


class BucketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bucket.objects.all()
    serializer_class = BucketDetailSerializer
