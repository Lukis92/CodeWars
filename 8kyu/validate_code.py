# https://www.codewars.com/kata/56a25ba95df27b7743000016/train/python
import re

def validate_code(code):
    return bool(re.match(r'^[123]', str(code)))

print(validate_code(248))