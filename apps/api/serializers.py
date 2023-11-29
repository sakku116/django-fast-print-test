from rest_framework import serializers

from .models import Product, Category, Status

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id_produk', 'nama_produk', 'harga', 'kategori', 'status')