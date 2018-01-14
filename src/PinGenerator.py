import random


class PinGenerator:
    @staticmethod
    def generate_pin():
        return random.SystemRandom().randint(1000, 8999)
