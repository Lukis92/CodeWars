# https://www.codewars.com/kata/58ef87dc4db9b24c6c000092/train/python
def sect_sort(arr, start, length=0):
    if not arr:
        return []
    
    end = start + length if length else len(arr)
    sorted_section = sorted(arr[start:end])
    arr[start:end] = sorted_section

    return arr
    
#print(sect_sort([1, 2, 5, 7, 4, 6, 3, 9, 8], 2))#, [1, 2, 3, 4, 5, 6, 7, 8, 9])
#print(sect_sort([1, 2, 5, 7, 4, 6, 3, 9, 8], 8))#, [1, 2, 5, 7, 4, 6, 3, 9, 8])
# sect_sort([9, 7, 4, 2, 5, 3, 1, 8, 6], 2, 5)#, [9, 7, 1, 2, 3, 4, 5, 8, 6])
print(sect_sort([1, 2, 5, 7, 4, 6, 3, 9, 8], 8, 3))#, [1, 2, 5, 7, 4, 6, 3, 9, 8])
# sect_sort([], 0)#, [])