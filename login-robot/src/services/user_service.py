from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass

class RegistrationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if self._user_repository.find_by_username(username):
            raise RegistrationError("Username already exists")

        if (not re.match('^[a-z]{3,}$', username)):
            raise RegistrationError("Username is invalid")

        if (not re.match('^[\S]{8,}$', password)):
            raise RegistrationError("Password is too short")
        
        if (not re.search('[^a-z]$', password)):
            raise RegistrationError("Password contains only letters")
