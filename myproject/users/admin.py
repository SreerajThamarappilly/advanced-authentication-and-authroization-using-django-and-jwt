# myproject/users/admin.py

from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Admin configuration for the User model.
    This allows managing Users through the Django Admin interface.
    """
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    ordering = ('email',)
