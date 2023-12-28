# https://www.codewars.com/kata/57e0206335e198f82b00001d/train/python
def esrever(st):
    return st[:-1][::-1]+st[-1] if st else ''

print(esrever('an Easy one?'))# 'eno ysaE na?'