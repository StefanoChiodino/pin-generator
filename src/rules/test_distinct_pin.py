def test_distinct_pin(pin, previous_pins):
    """ "It is distinct from the user's past three PINs (you may assume that a sufficient history is provided alongside
    the bank account details)" """
    if pin in previous_pins:
        raise ValueError(f"PIN '{pin}' is present in the user past 3 PINs.")
