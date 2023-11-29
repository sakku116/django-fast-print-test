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

        unique_categories = []
        unique_statuses = []
        for data in raw_data:
            print("-----------------------------")
            print(data.get("id_produk"))
            product_obj = Product.objects.create(
                id_produk=int(data.get("id_produk")),
                nama_produk=data.get("nama_produk"),
                harga=int(data.get("harga")),
            )

            category = data.get("kategori")
            if category and category not in unique_categories:
                unique_categories.append(category)

                category_obj = Category.objects.create(
                    nama_kategori=category,
                )
                category_obj.produk.add(product_obj)
                category_obj.save()

            status = data.get("status")
            if status and status not in unique_statuses:
                unique_statuses.append(status)

                status_obj = Status.objects.create(
                    nama_status=status,
                )
                status_obj.produk.add(product_obj)
                status_obj.save()

        self.stdout.write(self.style.SUCCESS('Data seeded successfully!'))
