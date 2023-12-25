# https://www.codewars.com/kata/5a043724ffe75fbab000009f/train/python
def reverse_middle(lst):
    mid = len(lst) // 2
    if len(lst) == 1:
        return lst
    elif len(lst) % 2 == 0:
        return lst[mid-1:mid+1][::-1]
    else:
        return lst[mid-1:mid+2][::-1]
\
print(reverse_middle([4, 3, 100, 1]))#, [100, 3]
print(reverse_middle([1, False, 'string', {}, 7.43]))#, [{}, 'string', False]