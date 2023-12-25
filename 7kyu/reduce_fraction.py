# https://www.codewars.com/kata/576400f2f716ca816d001614/train/python
from math import gcd

def reduce_fraction(fraction):
    num1, num2 = fraction
    divisor = gcd(num1, num2)

    return num1 // divisor, num2 // divisor

print(reduce_fraction((80, 120)))# (2, 3)