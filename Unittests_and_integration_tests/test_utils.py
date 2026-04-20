#!/usr/bin/env python3
"""Unit tests for utility functions in utils.py."""
import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """Test the memoization decorator."""

    def test_memoize(self):
        """Test that a method is memoized."""
        class TestClass:
            """Test class for memoization."""

            def a_method(self):
                """Return a constant value."""
                return 42

            @memoize
            def a_property(self):
                """Memoized property that calls a_method."""
                return self.a_method()

        with patch.object(
            TestClass, 'a_method', return_value=42
        ) as mock_a_method:
            test_instance = TestClass()
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            mock_a_method.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
