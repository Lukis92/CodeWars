# https://www.codewars.com/kata/5951d30ce99cf2467e000013/train/python
def pythagorean_triple(integers):
    integers.sort()

    return integers[0]**2 + integers[1]**2 == integers[2]**2