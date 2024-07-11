from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from books.models import Author, Book, Category, Publisher
from accounts.models import User


class AuthorsViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email="test@test.com", password="admin")
        self.client.force_authenticate(user=self.user)
        self.author = Author.objects.create(name="Author 1")
        self.url = reverse("books-api:authors-list")

    def test_get_authors(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_author(self):
        data = {"name": "Author 2"}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 2)
        self.assertEqual(Author.objects.get(id=response.data["id"]).name, "Author 2")


class BooksViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email="test@test.com", password="test")
        self.client.force_authenticate(user=self.user)
        self.publisher = Publisher.objects.create(
            name="Publisher 1", address="123 Street"
        )
        self.category = Category.objects.create(
            name="Category 1", description="A category"
        )
        self.book = Book.objects.create(
            title="Book 1",
            description="A book description",
            publisher=self.publisher,
            category=self.category,
            publish_date="2023-01-01",
            page_number=100,
        )
        self.url = reverse("books-api:books-list")

    def test_get_books(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        data = {
            "title": "Book 2",
            "description": "Another book description",
            "publisher": self.publisher.id,
            "category": self.category.id,
            "publish_date": "2024-01-01",
            "page_number": 200,
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data["id"]).title, "Book 2")


class CategoryViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email="test@test.com", password="admin")
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(
            name="Category 1", description="a category"
        )
        self.url = reverse("books-api:categories-list")

    def test_get_categories(self):
        response = self.client.get(self.url)
        self.assertEqual = (response.status_code, status.HTTP_200_OK)

    def test_create_category(self):
        data = {
            "name": "category 2",
            "description": " a second category",
        }

        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)
        self.assertEqual(Category.objects.get(id=response.data["id"]).name, "category 2")


class PublishersViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email="test@test.com", password="admin")
        self.client.force_authenticate(user=self.user)
        self.publisher = Publisher.objects.create(name="Publisher 1", address="123 Street")
        self.url = reverse('books-api:publishers-list')

    def test_get_publishers(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_publisher(self):
        data = {"name": "Publisher 2", "address": "456 Avenue"}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Publisher.objects.count(), 2)
        self.assertEqual(Publisher.objects.get(id=response.data['id']).name, 'Publisher 2')
