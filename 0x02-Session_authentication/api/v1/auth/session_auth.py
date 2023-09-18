#!/usr/bin/env python3
"""Sessions"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """Inherit from base Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates new  Sessions"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Return User"""
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        user = self.user_id_by_session_id.get(session_id)
        return user

    def current_user(self, request=None):
        """overload) that returns a User"""
        if request is None:
            return None
        cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie)
        user = User.get(user_id)
        return user
