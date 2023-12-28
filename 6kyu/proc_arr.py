# https://www.codewars.com/kata/584d05422609c8890f0000be/train/python
from itertools import permutations

def proc_arr(arr):

    unique_combinations = {int(''.join(combination)) for combination in permutations(arr)}

    return [len(unique_combinations), min(unique_combinations), max(unique_combinations)]


print(proc_arr(['1','2','2','3','2','3']))#,[60, 122233, 332221]