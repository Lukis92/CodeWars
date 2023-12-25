# https://www.codewars.com/kata/55ccdf1512938ce3ac000056/train/python
import re
def is_lock_ness_monster(string):
    return bool(re.match(r'(tree fiddy)|(3.50)|(three fifty)',string))

print(is_lock_ness_monster("Your girlscout cookies are ready to ship. Your total comes to tree fiddy"))# True)