from src.helpers import get_pin_digits


def test_consecutive_sequence(pin):
    """ "It must not contain a complete consecutive number sequence (eg 1234, 3456 are not allowed)" """
    digits = get_pin_digits(pin)
    for i in range(0, len(digits) - 1):
        if digits[i] + 1 != digits[i + 1]:
            return
    raise ValueError("PIN is made of a consecutive number sequence.")
