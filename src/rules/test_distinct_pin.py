def test_distinct_pin(pin, previous_pins):
    """ Raises ValueError if PIN is present in previous pins. """
    if pin in previous_pins:
        raise ValueError(f"PIN '{pin}' is present in the user past {len(previous_pins)} PINs.")
