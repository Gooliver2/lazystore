from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from product.filters import ProductFilter
from product.models import Product, ProductType
from product.serializers import ProductCreateUpdateSerializer, ProductSerializer, ProductTypeSerializer


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    filter_class = ProductFilter
    search_fields = ('name', 'description')
    ordering_fields = ('name', 'price', 'type')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductCreateUpdateSerializer
        return ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return ProductCreateUpdateSerializer
        return ProductSerializer


class UploadProductImageView(generics.UpdateAPIView):
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = ProductSerializer

    queryset = Product.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if 'file' not in request.data:
            return Response("No file object in request", status=400)
        instance.image = request.data['file']
        instance.save()
        return Response(self.serializer_class(instance, context={"request": request}).data)


class ProductTypeListView(generics.ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    filer_fields = ('name', )
    search_fields = ('name',)
    ordering_fields = ('name', )


class ProductTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class UploadProductTypeImageView(generics.UpdateAPIView):
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = ProductTypeSerializer

    queryset = ProductType.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if 'file' not in request.data:
            return Response("No file object in request", status=400)
        instance.image = request.data['file']
        instance.save()
        return Response(self.serializer_class(instance, context={"request": request}).data)
