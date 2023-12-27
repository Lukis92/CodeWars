# https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004/train/python
from collections import Counter

def highest_rank(arr):
    counter = Counter(arr)
    max_keys = [key for key, value in counter.items() if value == max(counter.values())]
    return max(max_keys)