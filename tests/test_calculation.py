import pytest
from app.calculation import Calculation
from app.calculation import CalculationFactory
from app.calculation import (
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
    PowerCalculation,
)
def test_calculation_is_abstract():
    with pytest.raises(TypeError):
        Calculation(1, 2)


def test_calculation_attributes_and_execute():
    class TestCalculation(Calculation):
        def execute(self):
            return super().execute()

    calculation = TestCalculation(5, 3)

    assert calculation.a == 5
    assert calculation.b == 3
    assert calculation.execute() is None


def test_register_calculation():
    @CalculationFactory.register_calculation("test")
    class TestCalculation(Calculation):
        def execute(self):
            return self.a + self.b

    calculation = CalculationFactory.create("test", 2, 3)

    assert isinstance(calculation, TestCalculation)
    assert calculation.execute() == 5


def test_factory_invalid_operation():
    with pytest.raises(ValueError, match="Unknown operation"):
        CalculationFactory.create("invalid", 1, 2)

@pytest.mark.parametrize(
    "operation,a,b,expected_class,expected_result",
    [
        ("add", 2, 3, AddCalculation, 5),
        ("subtract", 5, 3, SubtractCalculation, 2),
        ("multiply", 4, 3, MultiplyCalculation, 12),
        ("divide", 8, 2, DivideCalculation, 4),
        ("power", 2, 3, PowerCalculation, 8),
    ],
)
def test_factory_real_calculations(
    operation,
    a,
    b,
    expected_class,
    expected_result,
):
    calculation = CalculationFactory.create(operation, a, b)

    assert isinstance(calculation, expected_class)
    assert calculation.execute() == expected_result

def test_divide_calculation_by_zero():
    calculation = CalculationFactory.create("divide", 5, 0)

    with pytest.raises(ValueError, match="Division by zero"):
        calculation.execute()