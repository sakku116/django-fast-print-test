# myapp/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from apps.api.models import MyModel

class Command(BaseCommand):
    help = 'seed initial data and mapping it into the database'

    def handle(self, *args, **options):
        # Your data seeding logic here
        MyModel.objects.create(name='Example 1', description='Description 1')
        MyModel.objects.create(name='Example 2', description='Description 2')

        self.stdout.write(self.style.SUCCESS('Data seeded successfully!'))
