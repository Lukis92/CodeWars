# https://www.codewars.com/kata/57a37f3cbb99449513000cd8/train/python
import re
def get_number_from_string(string):
    return int("".join(re.findall(r'[0-9]', string)))

print(get_number_from_string("hell5o wor6ld"))