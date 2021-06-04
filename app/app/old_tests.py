from django.test import TestCase
from app.calc import add, sub


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_sub_numbers(self):
        """Test that two number are substract together"""
        self.assertEqual(sub(5, 11), 6)
