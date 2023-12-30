# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python
import unittest

def max_sequence(arr):
	max_so_far = current_max = 0

	for num in arr:
		current_max = max(0, current_max + num)
		max_so_far = max(max_so_far, current_max)
	return max_so_far

class TestMaxSequenct(unittest.TestCase):

	def test_case_1(self):
		self.assertEqual(max_sequence([]), 0)

	def test_case_2(self):
		self.assertEqual(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

if __name__ == "__main__":
	unittest.main()