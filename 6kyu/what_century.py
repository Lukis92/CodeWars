# https://www.codewars.com/kata/52fb87703c1351ebd200081f/train/python
def what_century(year_str):
    year = int(year_str)
    century = (year + 99) // 100

    if 10 <= century % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(century % 10, "th")

    return f"{century}{suffix}"

what_century(1234)