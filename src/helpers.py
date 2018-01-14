def get_pin_digits(pin):
    """ Return an array with the single digits of the pin. Heavily assumes the PIN is made up of 4 digits. """
    digits = []
    for i in range(1, 5):
        digit = pin % 10
        pin = int(pin / 10)
        digits = [digit] + digits
    return digits
