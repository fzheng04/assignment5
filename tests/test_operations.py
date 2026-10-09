import pytest
from app.operations import Operations


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (2.5, 3.5, 6.0),
        (-2.5, 3.5, 1.0),
    ]
)
def test_addition(a, b, expected):
    assert Operations.addition(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (0, 0, 0),
        (-5, -3, -2),
        (10.5, 5.5, 5.0),
        (-10.5, -5.5, -5.0),
    ]
)
def test_subtraction(a, b, expected):
    assert Operations.subtraction(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (0, 10, 0),
        (-2, -3, 6),
        (2.5, 4, 10.0),
        (-2.5, 4, -10.0),
    ]
)
def test_multiplication(a, b, expected):
    assert Operations.multiplication(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (9, 3, 3),
        (-10, 2, -5),
        (7.5, 2.5, 3.0),
    ]
)
def test_division(a, b, expected):
    assert Operations.division(a, b) == expected


def test_division_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        Operations.division(10, 0)

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 8),
        (5, 2, 25),
        (10, 0, 1),
        (4, 0.5, 2),
        (-2, 3, -8),
    ]
)
def test_power(a, b, expected):
    assert Operations.power(a, b) == expected