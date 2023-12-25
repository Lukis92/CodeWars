# https://www.codewars.com/kata/58e0cb3634a3027180000040/train/python
def sort_by_value_and_index(arr):
    return sorted(arr, key=lambda x, idx=enumerate(arr): x * (next(idx)[0] + 1))

sort_by_value_and_index([3, 56, 22, 37, 87, 88, 88, 85])
