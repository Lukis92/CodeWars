# https://www.codewars.com/kata/52705ed65de62b733f000064/train/python
def sort_list(sort_by, lst):
    return sorted(lst, key=lambda x: x[sort_by], reverse=True)

x = "b"
y = [
      {"a": 2, "b": 2},
      {"a": 3, "b": 40},
      {"a": 1, "b": 12}
    ]
print(sort_list(x, y))