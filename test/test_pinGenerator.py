from unittest import TestCase

from src.PinGenerator import PinGenerator



class TestPinGenerator(TestCase):
    def setUp(self):
        # This is the number of attempts necessary to offset the random nature of the pin.
        self.attempts = 100

    def test_generates_pin(self):
        pin = PinGenerator.generate_pin()
        self.assertIs(type(pin), int)

    def test_generates_4_digits_pin(self):
        """ "It should be 4 digits long" """
        # Seen the random nature of the pin generator better run 100 iterations.
        for _ in range(0, self.attempts):
            pin = PinGenerator.generate_pin()
            self.assertGreaterEqual(pin, 1000)
            self.assertLessEqual(pin, 9999)

    def test_pin_is_random(self):
        """ The randomness of the pin has not actually been specified in the spec but it's inferred. """
        # The pin is in a 9999-1000=8999 range, which means in theory we could give the same twice, but chances are low.
        # 10 attempts at getting a different pin to test randomness are given.
        previous_pin = PinGenerator.generate_pin()
        for _ in range(10):
            pin = PinGenerator.generate_pin()
            # If any of the pins were not equal then this test passes.
            if pin != previous_pin:
                return
            previous_pin = pin
        else:
            raise AssertionError("Pin is not random")

    def test_pin_does_not_contain_more_than_2_consecutive_numbers(self):
        """ "It must not contain more than two consecutive numbers (eg 1112, 1111 are not allowed; 1211 is allowed)" """
        # Seen the random nature of the pin generator better run 100 iterations.
        for _ in range(0, self.attempts):
            pin = PinGenerator.generate_pin()
