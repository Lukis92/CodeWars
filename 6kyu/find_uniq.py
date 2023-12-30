# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python
import unittest
from collections import Counter

def find_uniq(arr):
    frequency = Counter(arr)

    for elem, count in frequency.items():
        if count == 1:
            return elem

class TestFindUniq(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)

    def test_case_2(self):
        self.assertEqual(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)

    def test_case_3(self):
        self.assertEqual(find_uniq([ 3, 10, 3, 3, 3 ]), 10)

if __name__ == "__main__":
    unittest.main()