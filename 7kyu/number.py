# https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python
def number(lines):
    return [f"{i+1}: {item}" for i, item in enumerate(lines)]

print(number(["a", "b", "c"]))# ["1: a", "2: b", "3: c"]