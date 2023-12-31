#!/usr/bin/env python3
"""Hash password"""
import bcrypt
import uuid
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
    psswd = password.encode("utf-8")
    return bcrypt.hashpw(psswd, salt)


def _generate_uuid() -> str:
    """Generates UUID

    Returns:
        string uuid
    """
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """Validates User

        Args:
            email: User email
            password: User password

        Returns: True / False
        """
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                hashed = _hash_password(password)
                password = password.encode('utf-8')
                if bcrypt.checkpw(password, hashed):
                    return True
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Creates session ID

        Args:
            email: email for the user

        Returns:
            session id
        """
        session_id = _generate_uuid()
        try:
            user = self._db.find_user_by(email=email)
            user.session_id = session_id
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Get user from session_id"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Take a user_id and destroy that user's session and update their
        session_id attribute to None
        Args:
            user_id (int): user's id
        Return:
            None
        """
        try:
            self._db.update_user(user_id, session_id=None)
        except ValueError:
            return None
        return None

    def get_reset_password_token(self, email: str) -> str:
        """Resets password"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        reset_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """Update password of a user"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError()
        hashed = _hash_password(password)
        self._db.update_user(
                user.id,
                hashed_password=hashed,
                reset_token=None
                )
