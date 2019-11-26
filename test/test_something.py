import pytest
from code import something


def test_factorial_5():
    assert something.factorial(120)== 5

def test_factorial_6():
    assert something.factorial(720)== 6
