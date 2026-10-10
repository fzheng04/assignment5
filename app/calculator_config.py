import os

from dotenv import load_dotenv

from app.exceptions import ConfigurationError


class CalculatorConfig:
    """Load and validate calculator settings."""

    def __init__(self):
        load_dotenv()

        self.history_file = os.getenv(
            "CALCULATOR_HISTORY_FILE",
            "data/history.csv"
        )

        self.max_history = self._load_max_history()

        self.auto_save = self._load_boolean(
            os.getenv("CALCULATOR_AUTO_SAVE", "true")
        )

    def _load_max_history(self) -> int:
        value = os.getenv("CALCULATOR_MAX_HISTORY", "100")

        try:
            max_history = int(value)
        except ValueError as exc:
            raise ConfigurationError(
                "CALCULATOR_MAX_HISTORY must be an integer."
            ) from exc

        if max_history <= 0:
            raise ConfigurationError(
                "CALCULATOR_MAX_HISTORY must be greater than zero."
            )

        return max_history

    @staticmethod
    def _load_boolean(value: str) -> bool:
        value = value.strip().lower()

        if value in {"true", "1", "yes", "on"}:
            return True

        if value in {"false", "0", "no", "off"}:
            return False

        raise ConfigurationError(
            f"Invalid boolean configuration value: {value}"
        )