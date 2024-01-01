# https://www.codewars.com/kata/578fdcfc75ffd1112c0001a1/train/python
import unittest

def bin_rota(arr):
    return [elem for i, row in enumerate(arr) for elem in (row[::-1] if i % 2 != 0 else row)]


class TestBinRota(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(bin_rota([["Bob","Nora"],["Ruby","Carl"]]), ["Bob","Nora","Carl","Ruby"])

if __name__ == "__main__":
    unittest.main()