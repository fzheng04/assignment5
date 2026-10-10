from app.exceptions import (
    CalculatorError,
    ConfigurationError,
    OperationError,
    ValidationError,
)


def test_validation_error_inherits_calculator_error():
    error = ValidationError("bad input")

    assert isinstance(error, CalculatorError)


def test_operation_error_inherits_calculator_error():
    error = OperationError("bad operation")

    assert isinstance(error, CalculatorError)


def test_configuration_error_inherits_calculator_error():
    error = ConfigurationError("bad configuration")

    assert isinstance(error, CalculatorError)


def test_exception_messages():
    assert str(ValidationError("invalid")) == "invalid"
    assert str(OperationError("failed")) == "failed"
    assert str(ConfigurationError("config")) == "config"