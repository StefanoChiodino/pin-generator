from unittest import TestCase

from src.rules.consecutive_digits_rule import test_consecutive_digits


class TestRules(TestCase):
    def test_consecutive_digits(self):
        with self.assertRaises(ValueError):
            test_consecutive_digits(1111)
        with self.assertRaises(ValueError):
            test_consecutive_digits(1112)
        with self.assertRaises(ValueError):
            test_consecutive_digits(2223)
        with self.assertRaises(ValueError):
            test_consecutive_digits(9999)
