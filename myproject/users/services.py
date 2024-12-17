# myproject/users/services.py

"""
Service Layer:
Encapsulates business logic, making code cleaner and more testable.
"""
from .repositories import UserRepository
from .models import User

class UserService:
    """
    Provides an abstraction over user-related business logic.
    Uses the repository to handle data access.
    """

    def __init__(self, user_repository=None):
        self.user_repository = user_repository or UserRepository()

    def register_user(self, email: str, password: str) -> User:
        # Additional business rules (e.g. checking if user already exists) can go here
        # For millions of users, consider caching lookups, asynchronous tasks, etc.
        return self.user_repository.create_user(email, password)

    def get_user_by_email(self, email: str) -> User:
        return self.user_repository.get_user_by_email(email)
