#!/usr/bin/env python3
"""Auth Class """
from flask import request
from typing import List, TypeVar
import fnmatch


class Auth:
    """Class Auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Authenticates pathh"""
        if path is None or not excluded_paths:
            return True
        path = path.rstrip('/')
        for excluded_path in excluded_paths:
            excluded_path = excluded_paths.rstrip('/')
            if fnmatch.fnmatch(path, excluded_path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorises the header"""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers

    def current_user(self, request=None) -> TypeVar('User'):
        """gets current_user"""
        return None
