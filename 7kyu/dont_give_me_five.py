# https://www.codewars.com/kata/5813d19765d81c592200001a/train/python
import unittest

def dont_give_me_five(start,end):
    return len([x for x in range(start, end+1) if '5' not in str(x)])

class TestDontGiveMeFice(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(dont_give_me_five(1,9), 8)

    def test_case_2(self):
        self.assertEqual(dont_give_me_five(4,17), 12)

if __name__ == "__main__":
    unittest.main()