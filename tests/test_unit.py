import pytest
from calculator.main import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(5, 3) == 8

def test_subtract():
    calc = Calculator()
    assert calc.subtract(10, 4) == 6

def test_multiply():
    calc = Calculator()
    assert calc.multiply(6, 7) == 42

def test_divide():
    calc = Calculator()
    assert calc.divide(8, 2) == 4

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(5, 0)
