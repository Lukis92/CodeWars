# https://www.codewars.com/kata/56b5dc75d362eac53d000bc8/train/python
def calculate_string(st):

    allowed_chars = set("0123456789.+-*/")
    clean_string = ''.join(char for char in st if char in allowed_chars)
    result = str(round(eval(clean_string)))
    return result

calculate_string("gdfgdf234dg54gf*23oP42")