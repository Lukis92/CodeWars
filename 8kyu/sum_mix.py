# https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/python
import unittest

def sum_mix(arr):
    return sum(int(x) for x in arr)

def sum_mix_refactored(arr):
    return sum(map(int, arr))

class TestSumMix(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(sum_mix([9, 3, '7', '3']), 22)

    def test_case_2(self):
        self.assertEqual(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]), 42)

    def test_case_3(self):
        self.assertEqual(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']), 41)

    def test_case_4(self):
        self.assertEqual(sum_mix(['1', '5', '8', 8, 9, 9, 2, '3']), 45)

    def test_case_5(self):
        self.assertEqual(sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61)

if __name__ == "__main__":
    unittest.main()