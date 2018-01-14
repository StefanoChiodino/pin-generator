from src.helpers import get_pin_digits


def test_reverse_sequence(pin):
    """ Raise ValueError if reversed digits in the PIN are consecutive. """
    digits = get_pin_digits(pin)
    reverse_digits = digits[::-1]
    for i in range(0, len(reverse_digits) - 1):
        if reverse_digits[i] + 1 != reverse_digits[i + 1]:
            return
    raise ValueError("PIN is made of a reverse number sequence.")
