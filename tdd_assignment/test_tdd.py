import unittest
from unittest import TestCase

from tdd.py import validate_password
from tdd.py import validate_email
from tdd.py import validate_name
from tdd.py import validate_username
from tdd.py import validate_age


class TestValidation(TestCase):
    """Tests validity of user input"""
    def test_password_contains_uppercase_letter(self):
        self.assertTrue(validate_password('@Jose1'))
        self.assertFalse(validate_password('@Cici'))

   
    def test_password_contains_lowercase_letter(self):
        self.assertTrue(validate_password('@Jose1'))
        self.assertFalse(validate_password('@Cici'))

    
    def test_password_contains_a_digit(self):
        self.assertTrue(validate_password('@Jose1'))
        self.assertFalse(validate_password('@Cici'))

    
    def test_password_contains_special_character(self):
        self.assertTrue(validate_password('@Jose1))
        self.assertFalse(validate_password('@Cici'))

if __name__ == "__main__":
    unittest()

    