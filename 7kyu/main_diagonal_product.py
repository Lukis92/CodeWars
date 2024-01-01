# https://www.codewars.com/kata/551204b7509063d9ba000b45/train/python
import unittest

def main_diagonal_product(mat):
    product = 1
    for c in range(len(mat)):
        product *= mat[c][c]
    return product

class TestMainDiagonalProduct(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(main_diagonal_product([[1,0],[0,1]]), 1)

    def test_case_2(self):
        self.assertEqual(main_diagonal_product([[1,2,3],[4,5,6],[7,8,9]]), 45)

if __name__ == "__main__":
    unittest.main()