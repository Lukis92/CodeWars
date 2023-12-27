# https://www.codewars.com/kata/5a6225e5d8e145b540000127/train/python
from collections import Counter

def common(a, b, c):
    common_elements_sum = 0

    b_counter, c_counter = Counter(b), Counter(c)

    for elem in a:
        if b_counter[elem] > 0 and c_counter[elem] > 0:
            common_elements_sum += elem
            b_counter[elem] -= 1
            c_counter[elem] -= 1

    return common_elements_sum