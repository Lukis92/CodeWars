# https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7/train/python
import unittest

def make_upper_case(s):
    return s.upper()

class TestMakeUpperCase(unittest.TestCase):

    def test_cases(self):
        assert make_upper_case("hello") == "HELLO"

if __name__ == "__main__":
    unittest.main()