# src Directory

## Overview

The `src` directory serves as the top-level container for the core Python modules of a tracking system that manages daily financial spending and calorie intake. It contains a single subdirectory, `modules`, which organizes each module into its own subdirectory. This structure is designed to keep the codebase modular and maintainable for a larger project that may include additional directories (e.g., `tests`).

## Directory Structure

-   `modules/`: Contains subdirectories for each Python module of the tracking system.
    -   `record/`: Contains `Record.py`, defining the `Record` class for storing individual records with amount, date, and comment.
    -   `calculator/`: Contains `Calculator.py`, defining the `Calculator` base class for tracking records with a daily limit.
    -   `calories_calculator/`: Contains `Calories_Calculator.py`, extending `Calculator` to track daily calorie intake with specific limits and messaging.
    -   `cash_calculator/`: Contains `Cash_Calculator.py`, extending `Calculator` to track cash spending with conversion to USD, EUR, or RUB.

## Features

-   Store records with amount (representing money or calories), date, and comment attributes.
-   Track daily financial spending with customizable limits.
-   Track daily calorie intake with limits between 1000 and 3000 kcal and user-friendly messages.
-   Support cash tracking with conversion between RUB, USD, and EUR using fixed exchange rates.
-   Provide daily and weekly statistics for both financial and calorie tracking.
-   Enforce input validation across all modules.

## Requirements

-   Python 3.8 or higher.
-   No external dependencies beyond the Python standard library (`datetime`, `typing`).
-   All module files (`record.py`, `calculator.py`, `calories_calculator.py`, `cash_calculator.py`) must be in their respective subdirectories under `modules`.

## Usage

The modules in the `modules` subdirectories can be imported into a larger project for tracking financial spending or calorie intake. Below is an example of using the modules together:

```python
from src.modules.record.record import Record
from src.modules.calculator.calculator import Calculator
from src.modules.calories_calculator.calories_calculator import CaloriesCalculator
from src.modules.cash_calculator.cash_calculator import CashCalculator

# Create a record
record = Record(amount=500, date="2025-05-24", comment="Lunch")

# General tracking (e.g., for miscellaneous records)
calc = Calculator(limit=1000)
calc.add_record(record)
print(calc.get_today_stats())  # Output: Today: spent 500, remained 500

# Calorie tracking
calorie_calc = CaloriesCalculator(limit=2000)
calorie_calc.add_record(record)
print(calorie_calc.get_today_calories_remained())
# Output: Today you can eat something else, but with a total caloric content of no more than 1500 kcal

# Cash tracking with currency conversion
cash_calc = CashCalculator(limit=10000)
cash_calc.add_record(record)
print(cash_calc.get_today_cash_remained("USD"))
# Output: You have 63.02 USD left for today
```

## Module Details

-   **modules/record/Record.py**: Stores records with amount (money or calories), date, and comment. Validates inputs and handles date parsing.
-   **modules/calculator/Calculator.py**: Base class for tracking records with methods for adding records and calculating daily/weekly stats.
-   **modules/calories_calculator/Calories_Calculator.py**: Extends `Calculator` for calorie tracking with limits and user-friendly messages.
-   **modules/cash_calculator/Cash_Calculator.py**: Extends `Calculator` for cash spending with currency conversion (USD, EUR, RUB).

## Notes

-   The `src` directory contains only the `modules` subdirectory, with each module in its own subdirectory (e.g., `record/`, `calculator/`, etc.). Other directories (e.g., `tests`) may exist in the parent project structure.
-   Ensure each module file is in its respective subdirectory under `modules` for proper imports.
-   Refer to individual module docstrings for detailed API information.
