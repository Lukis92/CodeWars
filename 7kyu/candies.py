# https://www.codewars.com/kata/55466644b5d240d1d70000ba/train/python
def candies(lst):
    return sum([max(lst) - e for e in lst]) if len(lst) > 1 else -1


print(candies([5,8,6,4])) # 9