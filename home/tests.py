"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import unittest

# TODO: Configure your database in settings.py and sync before running tests.

class Test2(unittest.TestCase):
    """Tests for the application views."""

    # Django requires an explicit setup() when running tests in PTVS

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)