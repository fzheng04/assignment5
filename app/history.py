from pathlib import Path

import pandas as pd

from app.calculation import Calculation


class HistoryManager:
    """Manage calculator history with pandas."""

    COLUMNS = ["operation", "a", "b", "result"]

    def __init__(self):
        self._history = pd.DataFrame(columns=self.COLUMNS)

    @property
    def data(self) -> pd.DataFrame:
        """Return a copy of the current history."""
        return self._history.copy()

    def add(self, calculation: Calculation) -> None:
        """Add a completed calculation to history."""
        new_row = pd.DataFrame([calculation.to_dict()])
        self._history = pd.concat(
            [self._history, new_row],
            ignore_index=True
        )

    def clear(self) -> None:
        """Clear all calculation history."""
        self._history = pd.DataFrame(columns=self.COLUMNS)

    def save(self, file_path: str) -> None:
        """Save history to a CSV file."""
        path = Path(file_path)

        if path.parent != Path("."):
            path.parent.mkdir(parents=True, exist_ok=True)

        self._history.to_csv(path, index=False)

    def load(self, file_path: str) -> None:
        """Load history from a CSV file."""
        path = Path(file_path)

        if not path.exists():
            self.clear()
            return

        self._history = pd.read_csv(path)

    def replace(self, history: pd.DataFrame) -> None:
        """Replace the current history."""
        self._history = history.copy().reset_index(drop=True)

    def is_empty(self) -> bool:
        return self._history.empty

    def __len__(self) -> int:
        return len(self._history)