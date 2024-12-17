# myproject/users/urls.py

from django.urls import path
from .views import (
    UserRegisterView,
    CurrentUserView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView
)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('me/', CurrentUserView.as_view(), name='user-me'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
