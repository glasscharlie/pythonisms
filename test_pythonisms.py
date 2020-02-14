import pytest
from pythonisms import Pythonisms

def test_dunder_iter():
    ht = Pythonisms()
    ht.add('apple', 10)
    ht.add('banana', 101)
    actual = [item for item in ht if item]
    assert actual == [[['banana', 101]], [['apple', 10]]]