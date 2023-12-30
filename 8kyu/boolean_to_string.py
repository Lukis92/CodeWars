# https://www.codewars.com/kata/551b4501ac0447318f0009cd/train/python
import unittest

def boolean_to_string(b):
    return str(b)

class TestBooleanToString(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(boolean_to_string(True), "True")

    def test_case_2(self):
        self.assertEqual(boolean_to_string(False), "False")

if __name__ == "__main__":
    unittest.main()