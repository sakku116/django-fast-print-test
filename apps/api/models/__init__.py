from django.db import models

class Product(models.Model):
    id_produk = models.BigAutoField(primary_key=True)
    nama_produk = models.CharField(max_length=164)
    harga = models.IntegerField(default=0, max_length=164)

class Category(models.Model):
    id_kategori = models.BigAutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=164)
    produk = models.ForeignKey(Product, on_delete=models.CASCADE)

class Status(models.Model):
    id_status = models.BigAutoField(primary_key=True)
    nama_status = models.CharField(max_length=164)
    produk = models.ForeignKey(Product, on_delete=models.CASCADE)
