# Assignment 5 - Enhanced Calculator

## Overview

This project is an enhanced command-line calculator built in Python. It expands on the previous calculator assignments by using advanced object-oriented design patterns, pandas-based history management, configuration through environment variables, undo/redo support, and automated testing with GitHub Actions.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Power
- Root
- Interactive REPL interface
- Calculation history using pandas
- Save and load history using CSV files
- Automatic history saving
- Undo and redo
- Environment variable configuration
- Input validation and custom exceptions
- 100% automated test coverage

## Design Patterns

This project uses several software design patterns:

- **Strategy Pattern** - Each calculator operation is implemented as an interchangeable strategy.
- **Factory Pattern** - `OperationFactory` creates the appropriate operation object based on user input.
- **Observer Pattern** - Observers are notified after calculations for logging and automatic history saving.
- **Memento Pattern** - Calculator history states are saved so undo and redo can restore previous states.
- **Facade Pattern** - The `Calculator` class provides a simplified interface to the application's different subsystems.

## Project Structure

```text
app/
├── __init__.py
├── calculation.py
├── calculator.py
├── calculator_config.py
├── calculator_memento.py
├── calculator_repl.py
├── exceptions.py
├── history.py
├── input_validators.py
└── operations.py

tests/
├── test_calculation.py
├── test_calculator.py
├── test_calculator_config.py
├── test_calculator_memento.py
├── test_calculator_repl.py
├── test_exceptions.py
├── test_history.py
├── test_input_validators.py
└── test_operations.py