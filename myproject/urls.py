# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Simple view for the root URL
def home(request):
    """
    Root endpoint to display a welcome message or API documentation link.
    """
    return JsonResponse({
        "message": "Welcome to the Advanced Authentication and Authorization API.",
        "api_documentation": "Visit /api/users/ for API endpoints.",
        "admin_panel": "Visit /admin/ for admin access."
    })

urlpatterns = [
    path('', home),  # Add this line for the root URL
    path('admin/', admin.site.urls),
    path('api/users/', include('myproject.users.urls')),
]
