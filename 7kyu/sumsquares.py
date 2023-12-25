# https://www.codewars.com/kata/57882daf90b2f375280000ad/train/python
def sumsquares(lst):
    return sum(element ** 2 if not isinstance(element, list) else sumsquares(element) for element in lst)

l = [[1,2],3]
print(sumsquares(l)) # 14