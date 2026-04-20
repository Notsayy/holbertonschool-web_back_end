#!/usr/bin/env python3
"""Unit tests for client.py."""
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient."""

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the expected URL from org payload."""
        known_payload = {"repos_url": "https://api.github.com/orgs/google/repos"}

        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=PropertyMock,
            return_value=known_payload
        ):
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, known_payload["repos_url"])
