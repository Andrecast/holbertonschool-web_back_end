#!/usr/bin/env python3
""" Unittests and integration tests module.
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized, param
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """ Class for nested map access test.
    """
    @parameterized.expand([
        param(1, nested_map={"a": 1}, path=("a",)),
        param({"b": 2}, nested_map={"a": {"b": 2}}, path=("a",)),
        param(2, nested_map={"a": {"b": 2}}, path=("a", "b"))
    ])
    def test_access_nested_map(self, expected, nested_map, path):
        """ Method that test access nested map
            and returns what it is supposed to.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        param(KeyError, nested_map={}, path=("a",)),
        param(KeyError, nested_map={"a": 1}, path=("a", "b"))
    ])
    def test_access_nested_map_exception(self, expected, nested_map, path):
        """ Method that test acces nested map exception.
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Class for test get Json.
    """

    @parameterized.expand([
        param(test_url="http://example.com", test_payload={"payload": True}),
        param(test_url="http://holberton.io", test_payload={"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Returns a Mock object with a json method.
        """
        with unittest.mock.patch("utils.requests.get"):
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """ TestMemoize class.
    """

    def test_memoize(self):
        """ Method that test memoize """

        class TestClass:
            """ TestClass """

            def a_method(self):
                """ Method """
                return 42

            @memoize
            def a_property(self):
                """ Property """
                return self.a_method()
