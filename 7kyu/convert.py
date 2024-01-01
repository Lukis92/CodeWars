# https://www.codewars.com/kata/56b8b0ae1d36bb86b2000eaa/train/python
import unittest
from datetime import datetime

def convert(date):
    formatted_date = date.strftime("%H:%M:%S,%f")[:-3]
    return formatted_date

class TestConvert(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(convert(datetime(2016, 2, 8, 16, 42, 59)), "16:42:59,000")
    def test_case_2(self):
        self.assertEqual(convert(datetime(1951, 10, 31, 2, 2, 24, 399000)), "02:02:24,399")
    def test_case_3(self):
        self.assertEqual(convert(datetime(1523, 5, 29, 23, 2, 2, 9000)), "23:02:02,009")
    def test_case_4(self):
        self.assertEqual(convert(datetime(1, 1, 1, 1, 1, 1, 110000)), "01:01:01,110")
    def test_case_5(self):
        self.assertEqual(convert(datetime(9999, 9, 9, 9, 9, 9, 999999)), "09:09:09,999")
    def test_case_6(self):
        self.assertEqual(convert(datetime(2, 12, 30, 23, 59, 59, 875939)), "23:59:59,875")
    def test_case_7(self):
        self.assertEqual(convert(datetime(1850, 12, 30, 13, 39, 19)), "13:39:19,000")
    def test_case_8(self):
        self.assertEqual(convert(datetime(1978, 3, 18, 12, 0, 0, 0)), "12:00:00,000")
    def test_case_9(self):
        self.assertEqual(convert(datetime(1850, 12, 30, 11, 11, 11, 123939)), "11:11:11,123")
    def test_case_10(self):
        self.assertEqual(convert(datetime(1850, 12, 30, 0, 0, 0, 321939)), "00:00:00,321")

if __name__ == "__main__":
    unittest.main()