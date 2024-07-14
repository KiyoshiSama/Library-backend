from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from books.models import Author, Book, Category, Publisher
from accounts.models import User
from faker import Faker


class BaseViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.fake = Faker()
        self.user = User.objects.create_user(
            email=self.fake.email(), password=self.fake.password()
        )
        self.client.force_authenticate(user=self.user)


class AuthorsViewSetTestCase(BaseViewSetTestCase):
    def setUp(self):
        super().setUp()
        self.author = Author.objects.create(name="Author 1")
        self.url_list = reverse("books-api:authors-list")
        self.url_detail = reverse("books-api:authors-detail", args=[self.author.id])

    def test_get_authors(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_author(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.author.name)

    def test_create_author(self):
        data = {"name": "Author 2"}
        response = self.client.post(self.url_list, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 2)
        self.assertEqual(Author.objects.get(id=response.data["id"]).name, "Author 2")

    def test_create_author_invalid_data(self):
        data = {"name": ""}
        response = self.client.post(self.url_list, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_author(self):
        data = {"name": "Updated Author"}
        response = self.client.put(self.url_detail, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.author.refresh_from_db()
        self.assertEqual(self.author.name, "Updated Author")

    def test_update_author_invalid_data(self):
        data = {"name": ""}
        response = self.client.put(self.url_detail, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_author(self):
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.count(), 0)

    def test_unauthorized_access(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class BooksViewSetTestCase(BaseViewSetTestCase):
    def setUp(self):
        super().setUp()
        self.publisher = Publisher.objects.create(name="Publisher 1", address="123 Street")
        self.category = Category.objects.create(name="Category 1")
        self.book = Book.objects.create(
            title="Book 1",
            description="A book description",
            publisher=self.publisher,
            category=self.category,
            publish_date="2023-01-01",
            page_number=100,
            is_available = True

        )
        self.url_list = reverse("books-api:books-list")
        self.url_detail = reverse("books-api:books-detail", args=[self.book.id])

    def test_get_books(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_book(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book.title)

    def test_create_book(self):
        data = {
            "title": "Book 2",
            "description": "Another book description",
            "publisher": self.publisher.id,
            "category": self.category.id,
            "publish_date": "2024-01-01",
            "page_number": 200,
            "is_available" : True,
            "authors": [{"name": "Author 1"}, {"name": "Author 2"}],
        }

        response = self.client.post(self.url_list, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data["id"]).title, "Book 2")

    def test_create_book_invalid_data(self):
        data = {
            "title": "",
            "description": "Invalid book description",
            "publisher": self.publisher.id,
            "category": self.category.id,
            "publish_date": "2024-01-01",
            "page_number": 200,
            "is_available" : True,
            "authors": [{"name": "Author 1"}, {"name": "Author 2"}],
        }
        response = self.client.post(self.url_list, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_book(self):
        data = {
            "title": "Updated Book",
            "description": "Updated book description",
            "publisher": self.publisher.id,
            "category": self.category.id,
            "publish_date": "2024-01-01",
            "page_number": 150,
            "is_available" : True,
            "authors": [{"name": "Updated Author"}],
        }
        response = self.client.put(self.url_detail, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_update_book_invalid_data(self):
        data = {
            "title": "",
            "description": "Updated book description",
            "publisher": self.publisher.id,
            "category": self.category.id,
            "publish_date": "2024-01-01",
            "page_number": 150,
            "is_available" : True,
            "authors": [{"name": "Updated Author"}],
        }
        response = self.client.put(self.url_detail, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_book(self):
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_unauthorized_access(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class CategoriesViewSetTestCase(BaseViewSetTestCase):
    def setUp(self):
        super().setUp()
        self.category = Category.objects.create(name="Category 1")
        self.url_list = reverse("books-api:categories-list")
        self.url_detail = reverse("books-api:categories-detail", args=[self.category.id])

    def test_get_categories(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_category(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.category.name)

    def test_create_category(self):
        data = {"name": "Category 2"}
        response = self.client.post(self.url_list, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)
        self.assertEqual(Category.objects.get(id=response.data["id"]).name, "Category 2")

    def test_create_category_invalid_data(self):
        data = {"name": ""}
        response = self.client.post(self.url_list, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_category(self):
        data = {"name": "Updated Category"}
        response = self.client.put(self.url_detail, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, "Updated Category")

    def test_update_category_invalid_data(self):
        data = {"name": ""}
        response = self.client.put(self.url_detail, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_category(self):
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)

    def test_unauthorized_access(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PublishersViewSetTestCase(BaseViewSetTestCase):
    def setUp(self):
        super().setUp()
        self.publisher = Publisher.objects.create(name="Publisher 1", address="123 Street")
        self.url_list = reverse("books-api:publishers-list")
        self.url_detail = reverse("books-api:publishers-detail", args=[self.publisher.id])

    def test_get_publishers(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_publisher(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.publisher.name)

    def test_create_publisher(self):
        data = {"name": "Publisher 2", "address": "456 Avenue"}
        response = self.client.post(self.url_list, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Publisher.objects.count(), 2)
        self.assertEqual(Publisher.objects.get(id=response.data["id"]).name, "Publisher 2")

    def test_create_publisher_invalid_data(self):
        data = {"name": "", "address": "456 Avenue"}
        response = self.client.post(self.url_list, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_publisher(self):
        data = {"name": "Updated Publisher", "address": "456 Avenue"}
        response = self.client.put(self.url_detail, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.publisher.refresh_from_db()
        self.assertEqual(self.publisher.name, "Updated Publisher")

    def test_update_publisher_invalid_data(self):
        data = {"name": "", "address": "456 Avenue"}
        response = self.client.put(self.url_detail, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_publisher(self):
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Publisher.objects.count(), 0)

    def test_unauthorized_access(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)