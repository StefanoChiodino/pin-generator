import random

from src.validate_pin import validate_pin


class PinGenerator:
    @staticmethod
    def generate_pin():
        while True:
            # TODO: investigate if any stronger randomness is necessary/possible.
            pin = random.SystemRandom().randint(1000, 8999)
            # noinspection PyBroadException
            try:
                validate_pin(pin)
            except:
                pass
            else:
                return pin
