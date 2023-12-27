# https://www.codewars.com/kata/590148d79097384be600001e/train/python
def sort_by_guide(arr, guide):
    result = zip(arr, guide)
    new_list = []
    for index, pair in enumerate(result):
        if pair[1] != -1:
            new_list.insert(pair[1]-1, pair[0])
        else:
            new_list.insert(index, pair[0])
    print(new_list)
    return

sort_by_guide([56, 78, 3, 45, 4, 66, 2, 2, 4], [3, 1, -1, -1, 2, -1, 4, -1, 5])