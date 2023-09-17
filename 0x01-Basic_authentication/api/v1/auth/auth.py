#!/usr/bin/env python3
"""Auth Class """
from flask import request
from typing import List, TypeVar


class Auth:
    """Class Auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Authenticates pathh"""
        if path is None or not excluded_paths:
            return True
        path = path.rstrip('/')
        excluded_paths = [p.rstrip('/') for p in excluded_paths]
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorises the header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """gets current_user"""
        return None
