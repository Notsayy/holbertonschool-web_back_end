#!/usr/bin/env python3
"""Unit tests for client.py."""
import unittest
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClient class."""

    @patch('client.get_json')
    def test_org(self, mock_get_json):
        """Test that the org method returns the correct value."""
        mock_get_json.return_value = {"login": "holberton"}
        client = GithubOrgClient("holberton")
        self.assertEqual(client.org, {"login": "holberton"})
