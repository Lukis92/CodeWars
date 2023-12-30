# https://www.codewars.com/kata/5a34da5dee1aae516d00004a/train/python
import unittest

def get_matrix(n):
    #row creation
    row_values= []
    matrix = []
    for c in range(n):
        for r in range(n):
            row_values.append(r)
        matrix.append(row_values)
    print(matrix)

print(get_matrix(2))
# class TestGetMatrix(unittest.TestCase):

#     def test_case_1(self):
#         self.assertEqual(get_matrix(0), [])
#     def test_case_2(self):
#         self.assertEqual(get_matrix(1), [[1]])
#     def test_case_3(self):
#         self.assertEqual(get_matrix(2), [[1, 0], [0, 1]])
#     def test_case_4(self):
#         self.assertEqual(get_matrix(3), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
#     def test_case_5(self):
#         self.assertEqual(get_matrix(5), [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]])

# if __name__ == '__main__':
#     unittest.main()