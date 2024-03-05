import random

def password_generator(length = 8, capital = False, numbers = False, symbols = False):

    characters = list(range(97, 123))

    final_length = 8 if length <= 8 else 16 if length > 16 else length
    password = ''

    if capital:
        characters += list(range(65, 91))

    if numbers:
        characters += list(range(49, 58))

    if symbols:
        characters += list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97))

    while len(password) < final_length:
        password += chr(random.choice(characters))

    return password
