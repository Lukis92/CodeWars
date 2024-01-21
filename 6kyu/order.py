# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python
import unittest

def order(sentence: str) -> str:
    """
    Rearrange words in a sentence based on the digit found in each word.

    Args:
    sentence (str): The input sentence with words containing digits.

    Returns:
    str: The sentence with words rearranged based on the digits.
    """
    result = sorted(sentence.split(), key=lambda word: sorted(filter(str.isdigit, word)))
    return " ".join(result)

class TestOrder(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")

    def test_case_2(self):
        self.assertEqual(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")

    def test_case_3(self):
        self.assertEqual(order(""), "")

if __name__ == "__main__":
    unittest.main()