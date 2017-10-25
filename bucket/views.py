from rest_framework import generics

from bucket.models import Bucket
from bucket.serializers import BucketSerializer


class BucketListView(generics.ListCreateAPIView):
    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer


class BucketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer
