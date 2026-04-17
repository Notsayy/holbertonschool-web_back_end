#!/usr/bin/env python3
"""
Session authentication module
"""
from requests import request

from api.v1.auth.auth import Auth
from models import user
from models.user import User
import uuid


class SessionAuth(Auth):
    """
    Session authentication class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user_id
        """
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a User ID based on a Session ID
        """
        if session_id is None:
            return None
        if type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Returns a User instance based on a cookie value
        """
        if request is None:
            return None

        session_cookie_value = self.session_cookie(request)
        if session_cookie_value is None:
            return None

        user_id = self.user_id_for_session_id(session_cookie_value)
        if user_id is None:
            return None

        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """
        Deletes the user session / logout
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        del self.user_id_by_session_id[session_id]
        return True
