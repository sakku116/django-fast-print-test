# myapp/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from apps.api.models import Category, Product, Status
import json

class Command(BaseCommand):
    help = 'seed initial data and mapping it into the database'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Status.objects.all().delete()
        Category.objects.all().delete()
