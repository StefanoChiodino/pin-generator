from src.rules.test_consecutive_digits import test_consecutive_digits
from src.rules.test_consecutive_sequence import test_consecutive_sequence


def validate_pin(pin):
    test_consecutive_digits(pin)
    test_consecutive_sequence(pin)
