def get_pin_digits(pin):
    """ Return an array with the single digits of the pin. Heavily assumes the PIN is made up of 4 digits. """
    digits = []
    divisor = 10000
    for i in range(4):
        digit = pin % divisor
        digits += digit
        divisor /= 10
    return digits
