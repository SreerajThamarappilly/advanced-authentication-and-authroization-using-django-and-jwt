# myproject/users/urls.py

from django.urls import path
from rest_framework.response import Response
from rest_framework.views import APIView
from .views import (
    UserRegisterView,
    CurrentUserView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView
)

# View for listing API endpoints at /api/users/
class UsersRootView(APIView):
    """
    Root endpoint for listing all available API routes in the 'users' app.
    """
    def get(self, request):
        return Response({
            "register": "/api/users/register/",
            "me": "/api/users/me/",
            "token": "/api/users/token/",
            "token_refresh": "/api/users/token/refresh/"
        })

urlpatterns = [
    path('', UsersRootView.as_view(), name='users-root'),  # Add this root endpoint
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('me/', CurrentUserView.as_view(), name='user-me'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
