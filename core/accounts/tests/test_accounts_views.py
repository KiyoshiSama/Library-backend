from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from accounts.models import User
from faker import Faker


class RegisterUserAPIViewTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.fake = Faker()
        self.user = User.objects.create_user(
            email=self.fake.email(), password=self.fake.password()
        )
        self.url = reverse("accounts-api:create-account")
        self.client.force_authenticate(user=self.user)

    def test_register_user_valid_input(self):
        email = self.fake.email()
        password = self.fake.password()
        data = {
            "email": email,
            "password": password,
            "password1": password,
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(email=email).email, email)

    def test_register_user_invalid_email(self):
        password = self.fake.password()
        data = {
            "email": "",
            "password": password,
            "password1": password,
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_missing_password(self):
        email = self.fake.email()
        data = {
            "email": email,
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_without_authentication(self):
        email = self.fake.email()
        password = self.fake.password()
        self.client.logout()
        data = {
            "email": email,
            "password": password,
            "password1": password,
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class UserProfileViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.fake = Faker()
        self.user = User.objects.create_user(
            email=self.fake.email(),
            password=self.fake.password(),
            first_name= self.fake.first_name(),
            last_name=self.fake.first_name(),
        )
        self.client.force_authenticate(user=self.user)
        self.url_list = reverse("accounts-api:details-list")
        self.url_detail = reverse(
            "accounts-api:details-detail", kwargs={"pk": self.user.id}
        )

    def test_get_user_profiles_authenticated(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_user_profile_detail_authenticated(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], self.user.email)

    def test_get_user_profiles_unauthenticated(self):
        self.client.logout()
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_user_profile_detail_unauthenticated(self):
        self.client.logout()
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_user_profile_authenticated_valid_input(self):
        data = {
            "first_name": "Jane",
            "last_name": "Doe",
        }
        response = self.client.patch(self.url_detail, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, "Jane")
        self.assertEqual(self.user.last_name, "Doe")

    def test_update_user_profile_authenticated_invalid_input(self):
        email=self.fake.email()
        data = {
            "email": "",
        }
        response = self.client.patch(self.url_detail, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.user.refresh_from_db()
        self.assertNotEqual(self.user.email, email)

    def test_update_user_profile_unauthenticated(self):
        self.client.logout()
        data = {
            "first_name": "Jane",
            "last_name": "Doe",
        }
        response = self.client.patch(self.url_detail, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
