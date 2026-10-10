import pytest

from app.exceptions import ValidationError
from app.input_validators import (
    validate_input,
    validate_number,
    validate_operation,
)


@pytest.mark.parametrize(
    "value,expected",
    [
        ("5", 5.0),
        ("-3", -3.0),
        ("2.5", 2.5),
        ("0", 0.0),
    ],
)
def test_validate_number(value, expected):
    assert validate_number(value) == expected


def test_validate_number_invalid():
    with pytest.raises(
        ValidationError,
        match="'abc' is not a valid number."
    ):
        validate_number("abc")


@pytest.mark.parametrize(
    "operation",
    [
        "add",
        "subtract",
        "multiply",
        "divide",
        "power",
        "root",
    ],
)
def test_validate_operation(operation):
    valid_operations = {
        "add",
        "subtract",
        "multiply",
        "divide",
        "power",
        "root",
    }

    assert validate_operation(operation, valid_operations) == operation


def test_validate_operation_case_and_spaces():
    valid_operations = {"add"}

    assert validate_operation(" ADD ", valid_operations) == "add"


def test_validate_operation_invalid():
    with pytest.raises(
        ValidationError,
        match="Invalid operation: modulus"
    ):
        validate_operation("modulus", {"add", "subtract"})


def test_validate_input():
    operation, a, b = validate_input(
        ["multiply", "6", "7"]
    )

    assert operation == "multiply"
    assert a == 6.0
    assert b == 7.0


@pytest.mark.parametrize(
    "parts",
    [
        [],
        ["add"],
        ["add", "5"],
        ["add", "5", "3", "9"],
    ],
)
def test_validate_input_wrong_length(parts):
    with pytest.raises(
        ValidationError,
        match="Enter an operation followed by two numbers."
    ):
        validate_input(parts)


def test_validate_input_invalid_first_number():
    with pytest.raises(ValidationError):
        validate_input(["add", "hello", "3"])


def test_validate_input_invalid_second_number():
    with pytest.raises(ValidationError):
        validate_input(["add", "3", "hello"])