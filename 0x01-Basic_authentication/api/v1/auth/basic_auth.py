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
        """ returns the User instance"""
        if not isinstance(user_email, str) or not isinstance(
                user_pwd, str):
            return None
        users = User.search(user_email)
        if not users:
            return None
        user = user[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user
