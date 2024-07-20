import pytest
from rest_framework.test import APIClient
from accounts.models import User
from faker import Faker


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def fake():
    return Faker()


@pytest.fixture
def user(db):
    user = User.objects.create_user(
        email="testuser@example.com",
        password="TestPassword123",
        is_first_login=True,
        verification_code="12345",
    )
    return user


@pytest.fixture
def authenticated_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def user_data():
    return {
        "email": "user@example.com",
        "password": "password123",
        "first_name": "John",
        "last_name": "Doe"
    }

@pytest.fixture
def create_user(user_data):
    return User.objects.create_user(**user_data)

@pytest.fixture
def create_superuser(user_data):
    return User.objects.create_superuser(**user_data)
