#!/usr/bin/env python3
"""Basic auth """
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User
import base64


class BasicAuth(Auth):
    """
    BasicAuth inherit from auth
    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str
            ) -> str:
        """
        returns Base64 part of the Authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        res = authorization_header.split(" ")[1]
        return res

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        """Basic - Base64 decode """
        if base64_authorization_header is None:
            return None
        if not isinstance(
                base64_authorization_header,
                str):
            return None
        try:
            # Decode the Base64 string
            decoded_bytes = base64.b64decode(base64_authorization_header)
        except (base64.binascii.Error, TypeError):
            return None
        decode_str = decoded_bytes.decode("utf-8")
        return decode_str

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> (str, str):
        """returns the user email and password"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(
                decoded_base64_authorization_header,
                str):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        user = decoded_base64_authorization_header.split(":")
        return (user[0], user[1])

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str
            ) -> TypeVar('User'):
        """
        Returns the User instance
        Args:
            user_email: The user's email.
            user_pwd: The user's password.
        Returns:
            The User instance
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        users = User.search({"email" : user_email})
        if len(users) == 0 or not users:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns a User instance based on a received request
        """
        Auth_header = self.authorization_header(request)
        if Auth_header is not None:
            token = self.extract_base64_authorization_header(Auth_header)
            if token is not None:
                decoded = self.decode_base64_authorization_header(token)
                if decoded is not None:
                    email, psswd = self.extract_user_credentials(decoded)
                    if email is not None:
                        return self.user_object_from_credentials(email, psswd)
        return

    def extract_user_credentials(self, decoded_base64_authorization_header):
        """Allow password with """
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None
        token = self.extract_base64_authorization_header(auth_header)
        if token is None:
            return None
        decode = self.decode_base64_authorization_header(token)
        if decode is  None:
            return None
        email, passwd = self.extract_user_credentials(decode)
        if ":" in passwd:
            user = User.search({"email": email})
            self.is_valid_password(password)
            return user

