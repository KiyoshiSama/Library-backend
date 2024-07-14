import random
from django.core.management.base import BaseCommand
from books.models import Author, Book, Category, Publisher
from faker import Faker

category_list = ["hi-fi", "crime", "thriller", "horror"]


class Command(BaseCommand):
    help = "creating book info..."

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        authors = []

        for _ in range(5):
            author = Author.objects.create(name=self.fake.name())
            authors.append(author)

        for name in category_list:
            Category.objects.get_or_create(name=name)

        for _ in range(5):
            book = Book.objects.create(
                title=self.fake.sentence(),
                description=self.fake.paragraph(nb_sentences=5),
                publisher=Publisher.objects.create(
                    name=self.fake.company(), address=self.fake.address()
                ),
                category=Category.objects.get(name=random.choice(category_list)),
                publish_date=self.fake.date(),
                page_number=self.fake.random_int(min=100, max=1000),
                is_available = True
            )

            book.authors.add(random.choice(authors))
