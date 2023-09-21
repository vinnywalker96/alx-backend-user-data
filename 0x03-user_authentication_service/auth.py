#!/usr/bin/env python3
"""Hash password"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Hashed password

    Args:
        password: string to be hashed

    Returns:
        Hashed password
    """
    salt = bcrypt.gensalt()
    psswd = password.encode('utf-8')
    return bcrypt.hashpw(psswd, salt)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new User

        Args:
            email: The email of the user
            password: The password of the user

        Returns:
            User Object
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed = _hash_password(password)
            user = self._db.add_user(email, hashed)
            return user
        raise ValueError(f"User {email} already exists")