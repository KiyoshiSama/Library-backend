from django.urls import reverse, resolve
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.api.views import RegisterUserAPIView, UserProfileViewSet
from django.test import SimpleTestCase

class AccountsApiUrlsTestCase(SimpleTestCase):
    def test_token_create_url_resolves(self):
        url = reverse('accounts-api:token-obtain-pair')
        self.assertEqual(resolve(url).func.view_class, TokenObtainPairView)

    def test_token_refresh_url_resolves(self):
        url = reverse('accounts-api:token-refresh')
        self.assertEqual(resolve(url).func.view_class, TokenRefreshView)

    def test_create_account_url_resolves(self):
        url = reverse('accounts-api:create-account')
        self.assertEqual(resolve(url).func.view_class, RegisterUserAPIView)

    def test_account_details_list_url_resolves(self):
        url = reverse('accounts-api:account-details-list')
        self.assertEqual(resolve(url).func.cls, UserProfileViewSet)

    def test_account_details_detail_url_resolves(self):
        url = reverse('accounts-api:account-details-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.cls, UserProfileViewSet)
