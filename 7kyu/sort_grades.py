# https://www.codewars.com/kata/58a08e622e7fb654a300000e/train/python
grades = {'VB': 1, 'V0': 2, 'V0+': 3}
grades.update({f'V{i}': i + 3 for i in range(1, 18)})

def sort_grades(lst):
    try:
        return sorted(lst, key=lambda i: grades[i])
    except KeyError as e:
        raise ValueError(f"Invalid grade: {e}")

sort_grades(['V7', 'V12', 'V1'])