#!/usr/bin/env python3
"""Auth module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash a password string using bcrypt with a generated salt.

    Args:
        password: the plain-text password to hash

    Returns:
        A salted bcrypt hash of the password as bytes
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt)
