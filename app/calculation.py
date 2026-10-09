from abc import ABC, abstractmethod
from app.operations import Operations

class Calculation(ABC):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    @abstractmethod
    def execute(self) -> float:
        pass

class CalculationFactory:
    _calculations = {}

    @classmethod
    def register_calculation(cls, name):
        def decorator(calculation_class):
            cls._calculations[name] = calculation_class
            return calculation_class
        return decorator

    @classmethod
    def create(cls, operation: str, a: float, b: float):
        if operation not in cls._calculations:
            raise ValueError(f"Unknown operation: {operation}")

        calculation_class = cls._calculations[operation]
        return calculation_class(a, b)


@CalculationFactory.register_calculation("add")
class AddCalculation(Calculation):
    def execute(self) -> float:
        return Operations.addition(self.a, self.b)


@CalculationFactory.register_calculation("subtract")
class SubtractCalculation(Calculation):
    def execute(self) -> float:
        return Operations.subtraction(self.a, self.b)


@CalculationFactory.register_calculation("multiply")
class MultiplyCalculation(Calculation):
    def execute(self) -> float:
        return Operations.multiplication(self.a, self.b)


@CalculationFactory.register_calculation("divide")
class DivideCalculation(Calculation):
    def execute(self) -> float:
        return Operations.division(self.a, self.b)


@CalculationFactory.register_calculation("power")
class PowerCalculation(Calculation):
    def execute(self) -> float:
        return Operations.power(self.a, self.b)