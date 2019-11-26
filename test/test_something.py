import pytest
from code import something


def test_factorial_5():
    assert something.factorial(5)==120

def test_factorial_6():
    assert something.factorial(6)==720
