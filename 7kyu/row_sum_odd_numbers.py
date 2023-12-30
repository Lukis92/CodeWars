# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python
import unittest

def row_sum_odd_numbers(n):
    return n ** 3


class TestRowSumOddNumbers(unittest.TestCase):

    def test_case_1(self):
        assert row_sum_odd_numbers(1) == 1

    def test_case_2(self):
        assert row_sum_odd_numbers(2) == 8

    def test_case_3(self):
        assert row_sum_odd_numbers(13) == 2197

    def test_case_4(self):
        assert row_sum_odd_numbers(19) == 6859

    def test_case_5(self):
        assert row_sum_odd_numbers(41) == 68921

if __name__ == "__main__":
    unittest.main()