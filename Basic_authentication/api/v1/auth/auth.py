#!/usr/bin/env python3
"""Module for API authentication management."""
from flask import request
from typing import List, TypeVar


class Auth:
    """Class to manage API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determine if authentication is required for a given path.

        Args:
            path: The request path to check.
            excluded_paths: List of paths that do not require authentication.

        Returns:
            True if authentication is required, False otherwise.
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        normalized = path if path.endswith('/') else path + '/'
        return normalized not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """Retrieve the authorization header from the request.

        Args:
            request: The Flask request object.

        Returns:
            None always (to be implemented in subclasses).
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieve the current authenticated user.

        Args:
            request: The Flask request object.

        Returns:
            None always (to be implemented in subclasses).
        """
        return None
