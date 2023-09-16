#!/usr/bin/env python3
"""Auth Class """
from flask import request
from typing import List, TypeVar


class Auth:
    """Class Auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Authenticates pathh"""
        return False

    def authorization_header(self, request=None) -> str:
        """Authorises the header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """gets current_user"""
        return None
