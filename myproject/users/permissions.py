# myproject/users/permissions.py

from rest_framework import permissions

class IsAuthenticatedAndActive(permissions.BasePermission):
    """
    Custom permission: Only allow access to authenticated and active users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_active)
