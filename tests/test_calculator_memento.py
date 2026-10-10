import pandas as pd

from app.calculator_memento import CalculatorMemento, MementoManager


def make_history(values):
    return pd.DataFrame(values)


def test_memento_stores_copy():
    history = make_history(
        [{"operation": "add", "a": 1, "b": 2, "result": 3}]
    )

    memento = CalculatorMemento(history)

    history.loc[0, "result"] = 999

    saved_history = memento.get_history()

    assert saved_history.loc[0, "result"] == 3


def test_get_history_returns_copy():
    history = make_history(
        [{"operation": "add", "a": 1, "b": 2, "result": 3}]
    )

    memento = CalculatorMemento(history)

    first_copy = memento.get_history()
    first_copy.loc[0, "result"] = 100

    second_copy = memento.get_history()

    assert second_copy.loc[0, "result"] == 3


def test_undo_returns_previous_state():
    manager = MementoManager()

    old_history = make_history(
        [{"operation": "add", "result": 3}]
    )

    current_history = make_history(
        [
            {"operation": "add", "result": 3},
            {"operation": "multiply", "result": 12},
        ]
    )

    manager.save_state(old_history)

    restored = manager.undo(current_history)

    assert len(restored) == 1
    assert restored.iloc[0]["operation"] == "add"


def test_redo_returns_next_state():
    manager = MementoManager()

    first_history = make_history(
        [{"operation": "add", "result": 3}]
    )

    second_history = make_history(
        [
            {"operation": "add", "result": 3},
            {"operation": "multiply", "result": 12},
        ]
    )

    manager.save_state(first_history)

    manager.undo(second_history)

    restored = manager.redo(first_history)

    assert len(restored) == 2
    assert restored.iloc[1]["operation"] == "multiply"


def test_undo_with_empty_stack_returns_none():
    manager = MementoManager()

    history = pd.DataFrame()

    assert manager.undo(history) is None


def test_redo_with_empty_stack_returns_none():
    manager = MementoManager()

    history = pd.DataFrame()

    assert manager.redo(history) is None


def test_new_state_clears_redo_stack():
    manager = MementoManager()

    first = make_history(
        [{"operation": "add", "result": 3}]
    )

    second = make_history(
        [
            {"operation": "add", "result": 3},
            {"operation": "multiply", "result": 12},
        ]
    )

    manager.save_state(first)
    manager.undo(second)

    manager.save_state(first)

    assert manager.redo(first) is None


def test_clear_removes_saved_states():
    manager = MementoManager()

    history = make_history(
        [{"operation": "add", "result": 3}]
    )

    manager.save_state(history)
    manager.clear()

    assert manager.undo(history) is None
    assert manager.redo(history) is None