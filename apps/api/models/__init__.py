from django.db import models

class Product(models.Model):
    id_produk = models.BigIntegerField(primary_key=True, unique=True)
    nama_produk = models.CharField(max_length=164)
    harga = models.IntegerField(default=0)
    kategori = models.ForeignKey("Category", on_delete=models.CASCADE, db_column="id_kategori", null=True)
    status = models.ForeignKey("Status", on_delete=models.CASCADE, db_column="id_status", null=True)

class Category(models.Model):
    id_kategori = models.BigAutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=164)

class Status(models.Model):
    id_status = models.BigAutoField(primary_key=True)
    nama_status = models.CharField(max_length=164)