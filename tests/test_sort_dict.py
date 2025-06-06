import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '7kyu')))
from sort_dict import sort_dict


def test_sort_dict_example():
    assert sort_dict({1: 3, 2: 2, 3: 1}) == [(1, 3), (2, 2), (3, 1)]


def test_sort_dict_general():
    assert sort_dict({1: 2, 2: 3, 3: 1}) == [(2, 3), (1, 2), (3, 1)]
