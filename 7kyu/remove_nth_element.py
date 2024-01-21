# https://www.codewars.com/kata/5a7b3d08fd5777bf6a000121/train/python
import unittest

def remove_nth_element(lst, n):
    # Fix it
    lst_copy = lst[:]
    del lst_copy[n]
    return lst_copy

class TestRemoveNthElement(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(remove_nth_element([1, 2, 3, 4, 5], 4), [1, 2, 3, 4])

    def test_case_2(self):
        self.assertEqual(remove_nth_element([9, 7, 6, 9], 0), [7, 6, 9])

if __name__ == "__main__":
    unittest.main()