from django.urls import path, include
from .routers import router as accounts_router
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

app_name = "accounts-api"

urlpatterns = [
    path("token-create/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token-refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path('', include(accounts_router.urls)),
    path("create-account/", views.RegisterUserAPIView.as_view(), name="create-account"),
]
