# myproject/users/repositories.py

"""
Repository layer: Abstracts database operations.
This helps if we switch to a different data store or add caching in the future.
"""
from .models import User

class UserRepository:
    def create_user(self, email: str, password: str) -> User:
        user = User(email=email)
        user.set_password(password)
        user.save()
        return user

    def get_user_by_email(self, email: str) -> User:
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
