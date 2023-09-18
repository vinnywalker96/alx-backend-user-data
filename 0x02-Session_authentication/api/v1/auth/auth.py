#!/usr/bin/env python3
"""Auth Class """
from flask import request
from typing import List, TypeVar
import fnmatch
import os


class Auth:
    """Class Auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Authenticates pathh"""
        if path is None or not excluded_paths:
            return True
        path = path.rstrip('/')
        excluded_paths = [p.rstrip('/') if not p.endswith(
            '*') else p for p in excluded_paths]
        for excluded_path in excluded_paths:
            if excluded_path == '*' or path.startswith(
                    excluded_path[:-1]):
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

    def session_cookie(self, request=None):
        """Returns Cookie"""
        if request is None:
            return None
        session = os.environ.get('SESSION_NAME', '_my_session_id')
        return request.cookies.get(session)
