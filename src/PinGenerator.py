import random


class PinGenerator:
    @staticmethod
    def generate_pin():
        # TODO: investigate if any stronger randomness is necessary/possible.
        return random.SystemRandom().randint(1000, 8999)
