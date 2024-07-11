from django.test import TestCase
from accounts.models import User

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            "email": "user@test.com",
            "password": "testpassword",
            "first_name": "John",
            "last_name": "Doe"
        }
        self.superuser_data = {
            "email": "superuser@test.com",
            "password": "superpassword",
            "first_name": "Admin",
            "last_name": "User"
        }

    def test_create_user(self):
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(user.email, self.user_data["email"])
        self.assertTrue(user.check_password(self.user_data["password"]))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_verified)
        self.assertFalse(user.is_banned)

    def test_create_superuser(self):
        superuser = User.objects.create_superuser(**self.superuser_data)
        self.assertEqual(superuser.email, self.superuser_data["email"])
        self.assertTrue(superuser.check_password(self.superuser_data["password"]))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_verified)
        self.assertFalse(superuser.is_banned)

    def test_user_str(self):
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(str(user), self.user_data["email"])

    def test_create_user_without_email(self):
        with self.assertRaises(ValueError) as context:
            User.objects.create_user(email=None, password="testpassword")
        self.assertEqual(str(context.exception), "Wrong email!")

    def test_create_user_with_invalid_email(self):
        with self.assertRaises(ValueError) as context:
            User.objects.create_user(email="", password="testpassword")
        self.assertEqual(str(context.exception), "Wrong email!")

    def test_create_superuser_with_missing_fields(self):
        superuser = User.objects.create_superuser(
            email=self.superuser_data["email"],
            password=self.superuser_data["password"]
        )
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_verified)

    def test_default_values(self):
        user = User.objects.create_user(**self.user_data)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_verified)
        self.assertFalse(user.is_banned)
