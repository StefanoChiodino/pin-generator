def test_does_not_contain_account_number_or_sort_code(pin, account_number, sort_code):
    """ Throws ValueError if pin contains account number or sort code digits """
    if str(pin) in str(account_number):
        raise ValueError(f"PIN {pin} is contained in the account number.")
    if str(pin) in str(sort_code[0]) + str(sort_code[1]) + str(sort_code[2]):
        raise ValueError(f"PIN {pin} is contained in the sort code.")
