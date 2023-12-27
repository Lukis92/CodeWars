# https://www.codewars.com/kata/5bc463f7797b00b661000118/train/python
def is_possible(lst, goal):
    if goal < -10 or goal > 10:
        return False
    
    return is_possible_helper(lst, 0, 0, goal)

def is_possible_helper(lst, index, current_sum, goal):
    if index == len(lst):
        return current_sum == goal

    return is_possible_helper(lst, index + 1, current_sum + lst[index], goal) or \
           is_possible_helper(lst, index + 1, current_sum - lst[index], goal)

print(is_possible([1, 3], 2))
# is_possible([1, 3, 4, 6, 8], -2)
# is_possible([15, 2, 3], 10)
# is_possible([1, 5, 3, 2, 5], -2)