# https://www.codewars.com/kata/56a946cd7bd95ccab2000055/train/python
import re
def lowercase_count(strng):
    return len(re.findall(r'[a-z]', strng))

print(lowercase_count("abcABC123"))#, 3))    