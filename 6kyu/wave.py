# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python
import unittest

def wave(people: str) -> list:
    """
    Create a 'wave' effect by capitalizing each letter in the string one at a time.

    Args:
    people (str): The input string.

    Returns:
    list: A list of strings showing the wave effect.
    """
    return [people[:i] + people[i].upper() + people[i+1:] for i in range(len(people)) if people[i].isalpha()]

class TestWave(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(wave("hello"), ["Hello", "hEllo", "heLlo", "helLo", "hellO"])

    def test_case_2(self):
        self.assertEqual(wave("codewars"), ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"])

    def test_case_3(self):
        self.assertEqual(wave(""), [])

    def test_case_4(self):
        self.assertEqual(wave("two words"),["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"])

    def test_case_5(self):
        self.assertEqual(wave(" gap "), [" Gap ", " gAp ", " gaP "])

    def test_case_6(self):
        self.assertEqual(wave("a       b    "), ["A       b    ", "a       B    "])

    def test_case_7(self):
        self.assertEqual(wave("this is a few words"), ["This is a few words", "tHis is a few words", "thIs is a few words", "thiS is a few words", "this Is a few words", "this iS a few words", "this is A few words", "this is a Few words", "this is a fEw words", "this is a feW words", "this is a few Words", "this is a few wOrds", "this is a few woRds", "this is a few worDs", "this is a few wordS"])

if __name__ == "__main__":
    unittest.main()