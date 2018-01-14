from unittest import TestCase

from src.PinGenerator import PinGenerator


class TestPinGenerator(TestCase):
    def test_generates_pin(self):
        pin = PinGenerator.generate_pin()
        self.assertIs(type(pin), int)

    def test_generates_4_digits_pin(self):
        """ "It should be 4 digits long"
        Seen the random nature of the pin generator better run 100 iterations. """
        for _ in range(0, 100):
            pin = PinGenerator.generate_pin()
            self.assertGreaterEqual(pin, 1000)
            self.assertLessEqual(pin, 9999)
