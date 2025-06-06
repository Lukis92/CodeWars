import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '6kyu')))
from sort_array import sort_array


def test_sort_array_example():
    assert sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]


def test_sort_array_only_odds():
    assert sort_array([5, 3, 1]) == [1, 3, 5]


def test_sort_array_empty():
    assert sort_array([]) == []
