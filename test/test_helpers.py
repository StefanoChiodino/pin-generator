from unittest import TestCase

from src.helpers import get_pin_digits


class TestHelpers(TestCase):
    def test_get_pin_digits(self):
        pin = 1234
        digits = get_pin_digits(pin)
        self.assertEqual([1, 2, 3, 4], digits)
