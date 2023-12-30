# https://www.codewars.com/kata/57fb44a12b53146fe1000136/train/python
def balance(left, right):
    weight_map = {'!': 2, '?': 3}

    left_weight = sum(weight_map.get(char, 0) for char in left)
    right_weight = sum(weight_map.get(char, 0) for char in right)
    if left_weight > right_weight:
        return "Left"
    elif left_weight < right_weight:
        return "Right"
    else:
        return "Balance"

print(balance("",""))# , "Balance")
# print(balance("!!","??"))# , "Right")
# print(balance("!??","?!!"))# , "Left")
# print(balance("!?!!","?!?"))# , "Left")
# print(balance("!!???!????","??!!?!!!!!!!"))# , "Balance")