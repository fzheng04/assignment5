from app.exceptions import ValidationError


def validate_number(value: str) -> float:
    """Convert user input to a number."""
    try:
        return float(value)
    except ValueError as exc:
        raise ValidationError(
            f"'{value}' is not a valid number."
        ) from exc


def validate_operation(operation: str, valid_operations: set[str]) -> str:
    """Make sure the requested operation exists."""
    operation = operation.lower().strip()

    if operation not in valid_operations:
        raise ValidationError(
            f"Invalid operation: {operation}"
        )

    return operation


def validate_input(parts: list[str]) -> tuple[str, float, float]:
    """Validate a calculator command such as 'add 5 3'."""
    if len(parts) != 3:
        raise ValidationError(
            "Enter an operation followed by two numbers."
        )

    operation = parts[0]
    first_number = validate_number(parts[1])
    second_number = validate_number(parts[2])

    return operation, first_number, second_number