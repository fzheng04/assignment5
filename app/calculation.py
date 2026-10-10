from app.operations import OperationFactory


class Calculation:
    """Represents one calculator operation and its result."""

    def __init__(self, operation: str, a: float, b: float):
        self.operation = operation
        self.a = a
        self.b = b
        self.result = None

    def execute(self) -> float:
        """Create the requested operation strategy and execute it."""
        strategy = OperationFactory.create_operation(self.operation)
        self.result = strategy.execute(self.a, self.b)
        return self.result

    def to_dict(self) -> dict:
        """Convert the calculation into a dictionary for history storage."""
        return {
            "operation": self.operation,
            "a": self.a,
            "b": self.b,
            "result": self.result,
        }