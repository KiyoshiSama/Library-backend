from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from accounts.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterUserAPIViewTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email="test@test.com", password="am!383IR")
        self.url = reverse("accounts-api:create-account")
        self.client.force_authenticate(user=self.user)

    def test_register_user(self):
        data = {
            "email": "newuser@test.com",
            "password": "QWERTY123!@#",
            "password1": "QWERTY123!@#",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(
            User.objects.get(email="newuser@test.com").email, "newuser@test.com"
        )

    def test_register_user_without_authentication(self):
        self.client.logout()
        data = {"email": "newuser@test.com", "password": "newpassword"}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class UserProfileViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email="test@test.com", password="password")
        self.client.force_authenticate(user=self.user)
        self.url_list = reverse("accounts-api:account-details-list")
        self.url_detail = reverse(
            "accounts-api:account-details-detail", kwargs={"pk": self.user.id}
        )

    def test_get_user_profiles(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_profile_detail(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_profile(self):
        data = {
            "first_name": "NewFirstName",
            "last_name": "NewLastName",
        }
        response = self.client.patch(self.url_detail, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, "NewFirstName")
        self.assertEqual(self.user.last_name, "NewLastName")

    def test_update_user_profile_without_authentication(self):
        self.client.logout()
        data = {
            "first_name": "NewFirstName",
            "last_name": "NewLastName",
        }
        response = self.client.patch(self.url_detail, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
