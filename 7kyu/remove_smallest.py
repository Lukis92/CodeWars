# https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python
def remove_smallest(numbers):
    if not numbers:
        return []
    
    numbers_list = numbers[:]
    numbers_list.remove(min(numbers))
    return numbers_list

remove_smallest([1, 2, 3, 4, 5])#, [2, 3, 4, 5]

