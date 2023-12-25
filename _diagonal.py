# https://www.codewars.com/kata/5968fb556875980bd900000f/train/python
def diagonal(ar):
   n = len(ar)
   
   for s in range(2 * n - 1):
      print(s)


arr = [
 [4, 5, 7],
 [3, 9, 1],
 [7, 6, 2]
]

diagonal(arr)
# [2, 1, 6, 7, 9, 7, 5, 3, 4]

# 6
# 5
# 5
# 4
# 4
# 4
# 3
# 3