# https://www.codewars.com/kata/5592fc599a7f40adac0000a8/train/python
import unittest

def sum_diagonals(matrix):
    if len(matrix) == 1:
        if len(matrix[0]) == 1:
            return sum(matrix[0] + matrix[0])
        else:
            return 0

    return sum([matrix[i][i] for i in range(len(matrix))]) + sum([matrix[i][len(matrix)-1-i] for i in range(len(matrix))])


class TestSumDiagonals(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(sum_diagonals([[1,2,3], [4,5,6], [7,8,9]]), 1 + 5 + 9 + 3 + 5 + 7)

if __name__ == "__main__":
    unittest.main()