# https://www.codewars.com/kata/63f3c61dd27f3c07cc7978de/train/python
def compare(a, b):
    str_a, str_b = str(a), str(b)
    digits = []
    if str_a == str_b:
        return "100%"
    for a in str_a:
        if a in str_b and a not in digits:
            digits.append(a)
    similarity = (len(digits) / 2) * 100
    return f"{int(similarity)}%"

print(compare(81, 10))