# https://www.codewars.com/kata/589577f0d1b93ae32a000001/train/python
def sort_by_height(a):
    sorted_heights = sorted([height for height in a if height != -1])

    height_index = 0
    for elem in range(len(a)):
        if a[elem] != -1:
            a[elem] = sorted_heights[height_index]
            height_index += 1
    return a

sort_by_height([-1, 150, 190, 170, -1, -1, 160, 180])