import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '6kyu')))
from common import common


def test_common_basic():
    assert common([1, 2, 3], [5, 3, 2], [7, 3, 2]) == 5


def test_common_with_duplicates():
    assert common([1, 2, 2, 3], [2, 2, 2, 5], [2, 2, 3]) == 4
