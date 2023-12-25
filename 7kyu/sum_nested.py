# https://www.codewars.com/kata/5a15a4db06d5b6d33c000018/train/python
def sum_nested(lst):
    total = 0
    for element in lst:
        if isinstance(element, list):
            total += sum_nested(element)
        else:
            total += element
    return total
print(sum_nested([1, [2, [3, [4]]]]))