import pytest
from code import abcd


def test_factorial_5():
    assert abcd.factorial([5])==120

def test_factorial_6():
    assert abcd.factorial([6])==720
