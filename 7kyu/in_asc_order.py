# https://www.codewars.com/kata/56b7f2f3f18876033f000307/train/python

def in_asc_order(arr):
    return arr == sorted(arr)

print(in_asc_order([1,2,4,7,19])) # returns True
print(in_asc_order([1,2,3,4,5])) # returns True
print(in_asc_order([1,6,10,18,2,4,20])) # returns False)