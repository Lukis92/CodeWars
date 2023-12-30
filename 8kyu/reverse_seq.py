# https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/python
import unittest

def reverse_seq(n):
    return list(range(n, 0, -1))

class TestReverseSeq(unittest.TestCase):

    def test_case(self):
        self.assertEqual(reverse_seq(5),[5,4,3,2,1])

if __name__ == "__main__":
    unittest.main()