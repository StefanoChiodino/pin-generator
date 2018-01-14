from random import randint


class PinGenerator:
    @staticmethod
    def generate_pin():
        return randint(1000, 9999)
