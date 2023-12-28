# https://www.codewars.com/kata/538835ae443aae6e03000547/train/python
def add(n):
    def adder(x):
        return n + x

    return adder

print(add(1)(3))#, 4