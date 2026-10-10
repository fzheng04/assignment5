import pandas as pd


class CalculatorMemento:
    """Store a snapshot of calculator history."""

    def __init__(self, history: pd.DataFrame):
        self._history = history.copy(deep=True)

    def get_history(self) -> pd.DataFrame:
        """Return a copy of the stored history."""
        return self._history.copy(deep=True)


class MementoManager:
    """Manage calculator states for undo and redo."""

    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def save_state(self, history: pd.DataFrame) -> None:
        """Save the current state before a change."""
        self._undo_stack.append(CalculatorMemento(history))
        self._redo_stack.clear()

    def undo(self, current_history: pd.DataFrame):
        """Return the previous state, if one exists."""
        if not self._undo_stack:
            return None

        self._redo_stack.append(
            CalculatorMemento(current_history)
        )

        previous_state = self._undo_stack.pop()
        return previous_state.get_history()

    def redo(self, current_history: pd.DataFrame):
        """Return the next state, if one exists."""
        if not self._redo_stack:
            return None

        self._undo_stack.append(
            CalculatorMemento(current_history)
        )

        next_state = self._redo_stack.pop()
        return next_state.get_history()

    def clear(self) -> None:
        """Clear all stored undo and redo states."""
        self._undo_stack.clear()
        self._redo_stack.clear()