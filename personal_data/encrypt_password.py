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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks if a provided password matches a hashed password.

    Args:
        hashed_password: The hashed password to compare against.
        password: The plain-text password to verify.

    Returns:
        True if the password matches the hash, False otherwise.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
