# myapp/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from apps.api.models import Category, Product, Status
import json

class Command(BaseCommand):
    help = 'seed initial data and mapping it into the database'

    def handle(self, *args, **options):
        raw_data = []
        with open('product_seed.json', 'r') as f:
            raw_data = json.load(f)

        for data in raw_data:
            category = data.get("kategori")
            category_obj, _ = Category.objects.get_or_create(
                nama_kategori=category,
            )
            category_obj.save()

            status = data.get("status")
            status_obj, _ = Status.objects.get_or_create(
                nama_status=status,
            )
            status_obj.save()

            product_obj, _ = Product.objects.get_or_create(
                id_produk=int(data.get("id_produk")),
                defaults={
                    "nama_produk": data.get("nama_produk"),
                    "harga": int(data.get("harga")),
                    "kategori": category_obj,
                    "status": status_obj
                }
            )

            print(f"Product {product_obj.nama_produk} created")


        self.stdout.write(self.style.SUCCESS('Data seeded successfully!'))
