from django.test import TestCase
from books.models import Author, Book, Category, Publisher
from faker import Faker

class AuthorModelTestCase(TestCase):
    def setUp(self):
        self.fake = Faker()
        self.author = Author.objects.create(name=self.fake.name())

    def test_author_creation(self):
        self.assertEqual(self.author.name, str(self.author))
        self.assertTrue(isinstance(self.author, Author))

    def test_author_writed_books(self):
        category = Category.objects.create(name=self.fake.word())
        publisher = Publisher.objects.create(name=self.fake.company(), address=self.fake.address())
        book = Book.objects.create(
            title=self.fake.sentence(),
            description=self.fake.text(),
            publisher=publisher,
            category=category,
            publish_date=self.fake.date(),
            page_number=self.fake.random_int(min=1, max=1000),
        )
        self.author.writed_books.add(book)
        self.assertEqual(self.author.writed_books.count(), 1)
        self.assertEqual(self.author.writed_books.first().title, book.title)

class BookModelTestCase(TestCase):
    def setUp(self):
        self.fake = Faker()
        self.category = Category.objects.create(name=self.fake.word())
        self.publisher = Publisher.objects.create(name=self.fake.company(), address=self.fake.address())
        self.book = Book.objects.create(
            title=self.fake.sentence(),
            description=self.fake.text(),
            publisher=self.publisher,
            category=self.category,
            publish_date=self.fake.date(),
            page_number=self.fake.random_int(min=1, max=1000),
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, str(self.book))
        self.assertTrue(isinstance(self.book, Book))

    def test_book_default_ordering(self):
        self.assertEqual(self.book._meta.ordering, ["title"])

class CategoryModelTestCase(TestCase):
    def setUp(self):
        self.fake = Faker()
        self.category = Category.objects.create(name=self.fake.word())

    def test_category_creation(self):
        self.assertEqual(self.category.name, str(self.category))
        self.assertTrue(isinstance(self.category, Category))

    def test_category_default_ordering(self):
        self.assertEqual(self.category._meta.ordering, ["name"])

class PublisherModelTestCase(TestCase):
    def setUp(self):
        self.fake = Faker()
        self.publisher = Publisher.objects.create(name=self.fake.company(), address=self.fake.address())

    def test_publisher_creation(self):
        self.assertEqual(self.publisher.name, str(self.publisher))
        self.assertTrue(isinstance(self.publisher, Publisher))

    def test_publisher_default_ordering(self):
        self.assertEqual(self.publisher._meta.ordering, ["name"])
