# https://www.codewars.com/kata/58a30be22d5b6ca8d9000012/train/python
from math import gcd
from itertools import product

def gcd_matrix(a,b):
    gcd_list = [gcd(x, y) for x, y in product(a, b)]
    return round(sum(gcd_list) / len(gcd_list), 3)

print(gcd_matrix([1,2,3],[4,5,6]))