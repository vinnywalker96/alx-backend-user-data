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
        if not decode_base64_authorization_header:
            return (None, None)
        if not isinstance(
                decode_base64_authorization_header,
                str):
            return (None, None)
        credentials = decode_base64_authorization_header.split(
                ":", 1)
        if len(credentials) != 2:
            return (None, None)
        return (credentials[0], credentials[1])

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
        try:
            user = User.search({"email": user_email})
            if not user:
                return None
            for u in user:
                if u.is_valid_password(user_pwd):
                    return u
            return None
        except Exception:
            return None
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns a User instance based on a received request
        """
        Auth_header = authorization_header(request)
        if Auth:
            token = extract_base64_authorization_header(
                    token)
            if token:
                decode = decode_base64_authorization_header(
                        token)
            if decode:
                email, password = extract_user_credentials(
                        decode)
                if email:
                    return user_object_from_credentials(email, password)
        return None

    
