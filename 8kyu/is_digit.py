# https://www.codewars.com/kata/567bf4f7ee34510f69000032/train/python
import re
def is_digit(n):
    return str(n).isdigit() and len(str(n)) == 1

print(is_digit(""))#, False)
print(is_digit("7"))#, True)
print(is_digit(" "))#, False)
print(is_digit("a"))#, False)
print(is_digit("a5"))#, False)