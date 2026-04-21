#!/usr/bin/env python3
"""Unit tests for GithubOrgClient"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Mock) -> None:
        """Unit-test GithubOrgClient.public_repos"""
        test_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "mit"}},
        ]
        test_url = "https://api.github.com/orgs/test_org/repos"
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_url
            mock_get_json.return_value = test_payload

            client = GithubOrgClient("test_org")
            self.assertEqual(
                client.public_repos(),
                ["repo1", "repo2", "repo3"]
            )
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(test_url)
