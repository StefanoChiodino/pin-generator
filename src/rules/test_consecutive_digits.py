from src.helpers import get_pin_digits


def test_consecutive_digits(pin):
    """ Raise ValueError if 3 or more digits in the PIN are the same.  """
    digits = get_pin_digits(pin)
    if (digits[0] == digits[1] and digits[1] == digits[2]) or (digits[1] == digits[2] and digits[2] == digits[3]):
        raise ValueError(f"Too many consecutive digits in {pin}")
