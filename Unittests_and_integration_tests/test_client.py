#!/usr/bin/env python3
"""Unit tests for client module."""
import unittest
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(
        self,
        repo: dict,
        license_key: str,
        expected: bool
    ) -> None:
        """Unit-test GithubOrgClient.has_license"""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected
        )
