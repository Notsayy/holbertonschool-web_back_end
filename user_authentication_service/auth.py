#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
import uuid
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hash a password string using bcrypt with a generated salt."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt)


def _generate_uuid() -> str:
    """Generate a new UUID and return its string representation."""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with the given email and password."""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed = _hash_password(password)
            return self._db.add_user(email, hashed.decode("utf-8"))

    def valid_login(self, email: str, password: str) -> bool:
        """Validate login credentials."""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                password.encode("utf-8"),
                user.hashed_password.encode("utf-8")
            )
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a new session for the user with the given email.

        Args:
            email: the user's email address

        Returns:
            The newly generated session ID as a string,
            or None if the user does not exist
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None
