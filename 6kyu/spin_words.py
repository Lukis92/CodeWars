# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
import unittest

def spin_words(sentence):
    return " ".join(word[::-1] if len(word) >= 5 else word for word in sentence.split())

class TestSpinWords(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(spin_words("Welcome"), "emocleW")

    def test_case_2(self):
        self.assertEqual(spin_words("to"), "to")

    def test_case_3(self):
        self.assertEqual(spin_words("CodeWars"), "sraWedoC")

    def test_case_4(self):
        self.assertEqual(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")

    def test_case_5(self):
        self.assertEqual(spin_words("This sentence is a sentence"), "This ecnetnes is a ecnetnes")

if __name__ == "__main__":
    unittest.main()