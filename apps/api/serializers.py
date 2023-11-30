from rest_framework import serializers

from .models import Product, Category, Status

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id_kategori', 'nama_kategori', 'created_at', 'updated_at')

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id_status', 'nama_status', 'created_at', 'updated_at')

class ProductSerializer(serializers.ModelSerializer):
    kategori = CategorySerializer()
    status = StatusSerializer()

    class Meta:
        model = Product
        fields = ('id_produk', 'nama_produk', 'harga', 'kategori', 'status', "created_at", "updated_at")

