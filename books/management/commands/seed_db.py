from django.core.management.base import BaseCommand
from books.models import Books
import random

class Command(BaseCommand):
    help = 'Seed the database with mock data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Clearing Existing database and Seeding the database...'))

        # Clear existing data
        Books.objects.all().delete()

        # Seed with mock data
        for _ in range(20):
            title = f"Title {random.randint(1, 100)}"
            author_name = f"Author {random.randint(1, 100)}"
            language = random.choice(['en', 'sp', 'fr', 'ge', 'hi'])
            Books.objects.create(title=title, author_name=author_name, language=language)

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
