# https://www.codewars.com/kata/57e1e61ba396b3727c000251/train/python
import re
def string_clean(s):
    return re.sub(r"\d+", "", s)

print(string_clean("(E3at m2e2!!)"))#, "(Eat me!!)")