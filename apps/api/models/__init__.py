from django.db import models

class Product(models.Model):
    id_produk = models.BigIntegerField(primary_key=True, unique=True)
    nama_produk = models.CharField(max_length=164)
    harga = models.IntegerField(default=0)

class Category(models.Model):
    id_kategori = models.BigAutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=164)
    produk = models.ForeignKey(Product, on_delete=models.CASCADE, db_column="id_produk")

class Status(models.Model):
    id_status = models.BigAutoField(primary_key=True)
    nama_status = models.CharField(max_length=164)
    produk = models.ForeignKey(Product, on_delete=models.CASCADE, db_column="id_produk")
