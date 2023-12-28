# https://www.codewars.com/kata/58925dcb71f43f30cd00005f/train/python
from itertools import permutations

def latest_clock(a, b, c, d):
    numbers = [a, b, c, d]
    valid_times = []

    for combination in permutations(numbers):
        hours, mins = combination[:2], combination[2:]
        if (0 <= hours[0] <= 2) and (hours[0] != 2 or hours[1] < 4) and mins[0] < 6:
            valid_times.append(combination)

    latest_time = max(valid_times)
    return f"{latest_time[0]}{latest_time[1]}:{latest_time[2]}{latest_time[3]}"

# print(latest_clock(1, 9, 8, 3))# "19:38"

# print(latest_clock(9, 1, 2, 5)) # '21:59'
print(latest_clock(4, 0, 2, 6)) # '20:46'