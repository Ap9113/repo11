import pytest
from interactive_calculator.calculator import add, subtract, multiply, divide, power


def test_add():
    assert add(3, 4) == 7
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(-1, -1) == 0


def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(8, 2) == 4
    assert divide(5, 2) == 2.5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(9, 0.5) == 3
