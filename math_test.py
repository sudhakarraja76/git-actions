import pytest
from math import add, subtract

def test_add_basic():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-5, 3) == -2

def test_subtract():
    assert subtract(10, 3) == 7
