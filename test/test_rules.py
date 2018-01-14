from unittest import TestCase

from src.rules.test_consecutive_digits import test_consecutive_digits
from src.rules.test_consecutive_sequence import test_consecutive_sequence
from src.rules.test_distinct_pin import test_distinct_pin


class TestRules(TestCase):
    def test_consecutive_digits(self):
        """ "It must not contain more than two consecutive numbers (eg 1112, 1111 are not allowed; 1211 is allowed)" """
        with self.assertRaises(ValueError):
            test_consecutive_digits(1111)
        with self.assertRaises(ValueError):
            test_consecutive_digits(1112)
        with self.assertRaises(ValueError):
            test_consecutive_digits(2223)
        with self.assertRaises(ValueError):
            test_consecutive_digits(9999)

    def test_complete_consecutive_sequence(self):
        """ "It must not contain a complete consecutive number sequence (eg 1234, 3456 are not allowed)" """
        with self.assertRaises(ValueError):
            test_consecutive_sequence(1234)
        with self.assertRaises(ValueError):
            test_consecutive_sequence(3456)
        with self.assertRaises(ValueError):
            test_consecutive_sequence(6789)
        with self.assertRaises(ValueError):
            test_consecutive_sequence(4567)

    def test_distinct_from_past_3_pin(self):
        """ "It is distinct from the user's past three PINs (you may assume that a sufficient history is provided
        alongside the bank account details)" """
        with self.assertRaises(ValueError):
            test_distinct_pin(1234, [1234, 3455, 6535])
        with self.assertRaises(ValueError):
            test_distinct_pin(3455, [1234, 3455, 6535])
        with self.assertRaises(ValueError):
            test_distinct_pin(6535, [1234, 3455, 6535])