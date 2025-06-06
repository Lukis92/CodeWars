import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '7kyu')))
from common_ground import common_ground


def test_common_ground_basic():
    assert common_ground('eat chicken', 'eat chicken and rice') == 'eat chicken'


def test_common_ground_duplicates():
    assert common_ground('a b b', 'b a b') == 'b a'


def test_common_ground_none():
    assert common_ground('this is', 'there') == 'death'
