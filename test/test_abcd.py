import pytest
from code import abcd


def test_factorial_5():
    assert code.factorial([5])==120

def test_factorial_6():
    assert code.factorial([6])==720
