from src.helpers import get_pin_digits


def test_consecutive_digits(pin):
    """ "It must not contain more than two consecutive numbers (eg 1112, 1111 are not allowed; 1211 is allowed)"
    Throws Error. """
    digits = get_pin_digits(pin)
    if (digits[0] == digits[1] and digits[1] == digits[2]) or (digits[1] == digits[2] and digits[2] == digits[3]):
        raise ValueError(f"Too many consecutive digits in {pin}")
