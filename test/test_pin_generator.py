from random import randint
from unittest import TestCase

from src.PinGenerator import PinGenerator


class TestPinGenerator(TestCase):
    def setUp(self):
        # This is the number of attempts necessary to offset the random nature of the pin.
        self.attempts_for_randomly_generated = 100

    def test_generates_pin(self):
        pin = PinGenerator.generate_pin([], 0, (0, 0, 0))
        self.assertIs(type(pin), int)

    def test_generates_4_digits_pin(self):
        """ "It should be 4 digits long" """
        for _ in range(0, self.attempts_for_randomly_generated):
            pin = PinGenerator.generate_pin([], 0, (0, 0, 0))
            self.assertGreaterEqual(pin, 1000)
            self.assertLessEqual(pin, 9999)

    def test_pin_is_random(self):
        """ The randomness of the pin has not actually been specified in the spec but it's inferred. """
        # The pin is in a 9999-1000=8999 range, which means in theory we could give the same twice, but chances are low.
        # 10 attempts at getting a different pin to test randomness are given.
        previous_pin = PinGenerator.generate_pin([], 0, (0, 0, 0))
        for _ in range(10):
            pin = PinGenerator.generate_pin([], 0, (0, 0, 0))
            # If any of the pins were not equal then this test passes.
            if pin != previous_pin:
                return
            previous_pin = pin
        else:
            raise AssertionError("Pin is not random")

    def test_can_generate_pin_given_account_number_and_sort_code(self):
        """ Generic test to make sure that the positive workflow works. """
        for _ in range(0, self.attempts_for_randomly_generated):
            bank_account = randint(0, 99999999)
            sort_code = (randint(0, 99), randint(0, 99), randint(0, 99))
            previous_pins = [PinGenerator.generate_pin([], 0, (0, 0, 0)),
                             PinGenerator.generate_pin([], 0, (0, 0, 0)),
                             PinGenerator.generate_pin([], 0, (0, 0, 0))]
            # noinspection PyBroadException
            try:
                PinGenerator.generate_pin(previous_pins, bank_account, sort_code)
            except Exception as exception:
                self.fail(f"Exception '{exception}' raised generating a PIN.")
