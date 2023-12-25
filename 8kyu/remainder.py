# https://www.codewars.com/kata/524f5125ad9c12894e00003f/train/python
def remainder(a,b):
    if b == 0 and a >= 0 or a == 0 and b >= 0:
        return None
    elif a >= b:
        return a % b
    else:
        return b % a