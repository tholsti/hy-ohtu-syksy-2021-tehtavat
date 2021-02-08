from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class RegistrationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if (password != password_confirmation):
            raise RegistrationError("Password and confirmation do not match")
            
        if (not re.match('^[a-z]{3,}$', username)):
            raise RegistrationError("Username is invalid")

        if (not re.match('^[\S]{8,}$', password)):
            raise RegistrationError("Password is too short")
        
        if (not re.search('[^a-z]$', password)):
            raise RegistrationError("Password contains only letters")




user_service = UserService()
