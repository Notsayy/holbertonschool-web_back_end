#!/usr/bin/env python3
"""Module for Basic Authentication management."""
import base64
from typing import Optional, Tuple
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class that inherits from Auth."""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> Optional[str]:
        """Extract the Base64 part of the Authorization header.

        Args:
            authorization_header: The Authorization header value.

        Returns:
            The Base64 encoded part after 'Basic ', or None if invalid.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> Optional[str]:
        """Decode a Base64 encoded authorization header.

        Args:
            base64_authorization_header: The Base64 encoded string.

        Returns:
            The decoded UTF-8 string, or None if invalid.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
    ) -> Tuple[Optional[str], Optional[str]]:
        """Extract user email and password from a decoded Base64 header.

        Args:
            decoded_base64_authorization_header: The decoded Base64 string.

        Returns:
            A tuple (email, password), or (None, None) if invalid.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password
