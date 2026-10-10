from app.calculation import Calculation
from app.calculator_config import CalculatorConfig
from app.calculator_memento import MementoManager
from app.history import HistoryManager


class Calculator:
    """Facade that provides a simple interface to calculator features."""

    def __init__(self, config=None):
        self.config = config or CalculatorConfig()
        self.history = HistoryManager()
        self.mementos = MementoManager()

        # Load existing calculation history when the calculator starts.
        self.history.load(self.config.history_file)

    def calculate(self, operation: str, a: float, b: float) -> float:
        """Perform a calculation and add it to history."""
        calculation = Calculation(operation, a, b)
        result = calculation.execute()

        # Only save an undo state after a successful calculation.
        self.mementos.save_state(self.history.data)

        self.history.add(calculation)
        self._limit_history()

        return result

    def get_history(self):
        """Return the current calculation history."""
        return self.history.data

    def clear_history(self) -> None:
        """Clear calculation history while preserving undo state."""
        if self.history.is_empty():
            return

        self.mementos.save_state(self.history.data)
        self.history.clear()

    def save_history(self, file_path=None) -> None:
        """Save history to CSV."""
        path = file_path or self.config.history_file
        self.history.save(path)

    def load_history(self, file_path=None) -> None:
        """Load history from CSV."""
        path = file_path or self.config.history_file

        previous_history = self.history.data
        self.history.load(path)

        self.mementos.save_state(previous_history)

    def undo(self) -> bool:
        """Restore the previous calculator state."""
        previous_state = self.mementos.undo(self.history.data)

        if previous_state is None:
            return False

        self.history.replace(previous_state)
        return True

    def redo(self) -> bool:
        """Restore a previously undone calculator state."""
        next_state = self.mementos.redo(self.history.data)

        if next_state is None:
            return False

        self.history.replace(next_state)
        return True

    def _limit_history(self) -> None:
        """Keep history within the configured maximum size."""
        if len(self.history) > self.config.max_history:
            limited_history = self.history.data.tail(
                self.config.max_history
            )
            self.history.replace(limited_history)