from src.rules.test_consecutive_digits import test_consecutive_digits
from src.rules.test_consecutive_sequence import test_consecutive_sequence
from src.rules.test_distinct_pin import test_distinct_pin
from src.rules.test_does_not_contain_account_number_or_sort_code import \
    test_does_not_contain_account_number_or_sort_code


def validate_pin(pin, previous_3_pins, account_number, sort_code):
    test_consecutive_digits(pin)
    test_consecutive_sequence(pin)
    test_distinct_pin(pin, previous_3_pins)
    test_does_not_contain_account_number_or_sort_code(pin, account_number, sort_code)
