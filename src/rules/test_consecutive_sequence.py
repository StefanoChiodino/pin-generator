from src.helpers import get_pin_digits


def test_consecutive_sequence(pin):
    """ Raise ValueError if 3 or more digits in the PIN are consecutive. """
    digits = get_pin_digits(pin)
    for i in range(0, len(digits) - 1):
        if digits[i] + 1 != digits[i + 1]:
            return
    raise ValueError("PIN is made of a consecutive number sequence.")
