#!/usr/bin/env python3
"""
Module for filtering and logging personal data (PII),
managing database connections, and hashing passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password with bcrypt and a random salt.

    Args:
        password: The plain-text password to hash.

    Returns:
        The salted, hashed password as bytes.
    """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())
    return hashed
