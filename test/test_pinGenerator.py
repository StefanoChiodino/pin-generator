from unittest import TestCase

from src.PinGenerator import PinGenerator


class TestPinGenerator(TestCase):
    def test_generates_pin(self):
        pin = PinGenerator.generate_pin()
        self.assertIs(type(pin), int)
