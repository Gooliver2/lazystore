from rest_framework import generics

from bucket.filters import BucketFilter
from bucket.models import Bucket
from bucket.serializers import BucketSerializer


class BucketListView(generics.ListCreateAPIView):
    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer
    filter_class = BucketFilter
    search_fields = ('card__uid', )
    ordering_fields = ('status', 'created_at', 'updated_at')


class BucketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer
