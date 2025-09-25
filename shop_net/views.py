from rest_framework import viewsets, generics
from .serializers import ProductSerializer, NetworkNodeSerializer
from .models import Product, NetworkNode
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class NetworkNodeViewSet(viewsets.ModelViewSet):
    serializer_class = NetworkNodeSerializer
    queryset = NetworkNode.objects.all()

    filter_backends = [DjangoFilterBackend,]

    filterset_fields = ['country',]
