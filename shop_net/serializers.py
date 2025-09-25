from rest_framework import serializers
from .models import Product, NetworkNode


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class NetworkNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        fields = ('id', 'name', 'email', 'country', 'city', 'street', 'home_number', 'products', 'supplier', 'debt', 'created_at')
        read_only_fields = ('debt',)
