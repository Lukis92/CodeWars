# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
import unittest

# def make_readable(seconds):
#     hours = seconds // 3600
#     minutes = (seconds - (hours * 3600)) // 60
#     seconds = seconds - (hours * 3600) - (minutes * 60)
#     return f"{hours:02}:{minutes:02}:{seconds:02}"

# Refactored version
def make_readable(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

class TestMakeReadable(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(make_readable(0), "00:00:00")

    def test_case_2(self):
        self.assertEqual(make_readable(5), "00:00:05")

    def test_case_3(self):
        self.assertEqual(make_readable(60), "00:01:00")

    def test_case_4(self):
        self.assertEqual(make_readable(86399), "23:59:59")

    def test_case_5(self):
        self.assertEqual(make_readable(359999), "99:59:59")

if __name__ == "__main__":
    unittest.main()