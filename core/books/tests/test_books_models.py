from django.test import TestCase
from books.models import Author, Book, Category, Publisher


class AuthorModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Author 1")

    def test_author_creation(self):
        self.assertEqual(self.author.name, "Author 1")
        self.assertEqual(str(self.author), "Author 1")

    def test_author_writed_books(self):
        category = Category.objects.create(name="Category 1", description="A category")
        publisher = Publisher.objects.create(name="Publisher 1", address="123 Street")
        book = Book.objects.create(
            title="Book 1",
            description="A book description",
            publisher=publisher,
            category=category,
            publish_date="2023-01-01",
            page_number=100,
        )
        self.author.writed_books.add(book)
        self.assertEqual(self.author.writed_books.count(), 1)
        self.assertEqual(self.author.writed_books.first().title, "Book 1")
