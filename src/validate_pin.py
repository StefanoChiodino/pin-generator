from src.rules.test_consecutive_digits import test_consecutive_digits
from src.rules.test_consecutive_sequence import test_consecutive_sequence
from src.rules.test_distinct_pin import test_distinct_pin


def validate_pin(pin, previous_3_pins):
    test_consecutive_digits(pin)
    test_consecutive_sequence(pin)
    test_distinct_pin(pin, previous_3_pins)
