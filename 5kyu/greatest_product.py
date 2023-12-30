# https://www.codewars.com/kata/529872bdd0f550a06b00026e/train/python
import math

def greatest_product(st):
    largest_product = 0
    for i in range(len(st) - 4):
        digits = st[i:i+5]
        product = math.prod(int(d) for d in digits)
        largest_product = max(largest_product, product)
    return largest_product
print(greatest_product("123834539327238239583"))#, 3240)