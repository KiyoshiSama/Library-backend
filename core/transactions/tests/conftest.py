import pytest
from datetime import timedelta
from faker import Faker
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.cache import cache
from transactions.models import Checkout, Hold
from books.models import Author, Book, Publisher, Category

User = get_user_model()

faker = Faker()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture(autouse=True)
def clear_cache():
    cache.clear()


@pytest.fixture
def user(db):
    user = User.objects.create_user(
        email=faker.email(),
        password=faker.password(),
    )
    return user


@pytest.fixture
def authenticated_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def authors():
    return [Author.objects.create(name=faker.name()) for _ in range(2)]


@pytest.fixture
def book(authors):
    book = Book.objects.create(
        title=faker.word(),
        description=faker.text(),
        publisher=Publisher.objects.create(
            name=faker.company(), address=faker.address()
        ),
        category=Category.objects.create(name=faker.word()),
        publish_date=faker.date(),
        page_number=faker.random_number(),
        is_available=True,
    )
    book.authors.set(authors)
    return book


@pytest.fixture
def checkout(db, user, book):
    checkout = Checkout.objects.create(
        start_time=timezone.now().date(),
        end_time=(timezone.now() + timedelta(days=14)).date(),
        book=book,
        customer=user,
        is_returned=False,
    )
    return checkout


@pytest.fixture
def hold(db, user, book):
    hold = Hold.objects.create(
        start_time=timezone.now().date(),
        end_time=(timezone.now() + timedelta(days=14)).date(),
        book=book,
        customer=user,
    )
    return hold
