# https://www.codewars.com/kata/52a112d9488f506ae7000b95/train/python
def is_int_array(arr):
    if not isinstance(arr, list):
        return False

    for a in arr:
        if not isinstance(a, int):
            if not (isinstance(a, float) and a.is_integer()):
                return False
    return True

print(is_int_array([1.00, 2, 3, 4]))
# print(is_int_array(None))