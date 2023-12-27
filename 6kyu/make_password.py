# https://www.codewars.com/kata/5b3d5ad43da310743c000056/train/python
import random
import string
def make_password(length, flag_upper, flag_lower, flag_digit):
    upper_chars = string.ascii_uppercase
    lower_chars = string.ascii_lowercase
    digits = string.digits

    password_chars = []
    if flag_upper:
        password_chars.append(random.choice(upper_chars))
    if flag_lower:
        password_chars.append(random.choice(lower_chars))
    if flag_digit:
        password_chars.append(random.choice(digits))

    all_allowed_chars = ""
    if flag_upper:
        all_allowed_chars += upper_chars
    if flag_lower:
        all_allowed_chars += lower_chars
    if flag_digit:
        all_allowed_chars += digits

    while len(password_chars) < length:
        char = random.choice(all_allowed_chars)
        if char not in password_chars:
            password_chars.append(char)

    random.shuffle(password_chars)

    return "".join(password_chars)



make_password(5, True, False, False)