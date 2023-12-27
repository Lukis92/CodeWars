# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python
def sort_array(source_array):
    odd_list = []
    for elem in source_array:
        if elem % 2 != 0:
            odd_list.append(elem)
    odd_list.sort()
    odd_index = 0
    for index, elem in enumerate(source_array):
        if elem % 2 != 0:
            source_array[index] = odd_list[odd_index]
            odd_index += 1
    return source_array

print(sort_array([5, 3, 2, 8, 1, 4])) #[1, 3, 2, 8, 5, 4]