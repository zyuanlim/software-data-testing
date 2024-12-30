import pytest

from src.base.basic_examples import Calculator, square


def test_square():
    assert square(2) == 4


@pytest.mark.parametrize("input, expected", [(2, 4), (3, 9), (4, 16)])
def test_squares(input, expected):
    assert square(input) == expected


@pytest.fixture
def calculator():
    return Calculator()


def test_calculator_add(calculator):
    assert calculator.add(5) == 5
    assert calculator.add(3) == 8
    assert calculator.add(-2) == 6
    assert calculator.add(0) == 6


def test_calculator_multiply(calculator):
    assert calculator.multiply(4) == 4
    assert calculator.multiply(2) == 8
    assert calculator.multiply(3) == 24
    assert calculator.multiply(0.5) == 12


# test combined add and multiply operations
def test_calculator_combined_operations(calculator):
    pass
