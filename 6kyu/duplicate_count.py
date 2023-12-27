# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python
from collections import Counter

def duplicate_count(text):
    char_counter = Counter(list(text.lower()))
    duplicates = sum(1 for v in char_counter.values() if v > 1)
    return duplicates

duplicate_count("abcdeaB")