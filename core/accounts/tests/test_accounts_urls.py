import pytest
from django.urls import reverse, resolve
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.api.views import (
    RegisterUserAPIView,
    ActiveAccountGenericApiView,
    UserProfileGenericView,
)


@pytest.mark.django_db
def test_register_user_url():
    url = reverse("accounts-api:create-account")
    assert resolve(url).func.view_class == RegisterUserAPIView


@pytest.mark.django_db
def test_active_account_url():
    url = reverse("accounts-api:active-account")
    assert resolve(url).func.view_class == ActiveAccountGenericApiView


@pytest.mark.django_db
def test_user_profile_url():
    url = reverse("accounts-api:accounts")
    assert resolve(url).func.view_class == UserProfileGenericView


@pytest.mark.django_db
def test_token_create_url():
    url = reverse("accounts-api:token-obtain-pair")
    assert resolve(url).func.view_class == TokenObtainPairView


@pytest.mark.django_db
def test_token_refresh_url():
    url = reverse("accounts-api:token-refresh")
    assert resolve(url).func.view_class == TokenRefreshView
