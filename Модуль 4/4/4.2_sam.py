import re

def check_symbols(value):
    symbols_pattern = r"[<>,*&^%$#@!-=+'0-9]"
    symbols_found = re.findall(symbols_pattern, value)
    if len(symbols_found) == 0:
        print("Add some symbols or numbers")
        return False
    else:
        return True

def validate_password(value):
    password_length = len(value)
    if password_length > 6 and check_symbols(value):
        print("Your password is good!")
    else:
        print("Your password is not good enough...")

value = input('Enter a password to check: ')
validate_password(value)