"""
Sample Test
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        res = calc.Add(2, 3);
        self.assertEqual(res, 5);