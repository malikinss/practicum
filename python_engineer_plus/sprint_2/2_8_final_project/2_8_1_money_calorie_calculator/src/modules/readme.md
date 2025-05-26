# modules Directory

## Overview

The `modules` directory contains the core Python modules for a tracking system that manages both daily financial spending and calorie intake.
It includes four modules designed to work together for recording transactions, enforcing daily limits, and supporting currency conversion for cash tracking and calorie-specific messaging.
These modules are intended to be imported into a larger project that may include additional directories (e.g., `tests`).

## Directory Structure

-   `record.py`: Defines the `Record` class for storing individual records with amount, date, and comment.
-   `calculator.py`: Defines the `Calculator` base class for tracking records with a daily limit.
-   `calories_calculator.py`: Extends `Calculator` to track daily calorie intake with specific limits and messaging.
-   `cash_calculator.py`: Extends `Calculator` to track cash spending with conversion to USD, EUR, or RUB.

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
-   All modules (`record.py`, `calculator.py`, `calories_calculator.py`, `cash_calculator.py`) must be in the same directory.

## Usage

These modules can be imported into a larger project for tracking financial spending or calorie intake. Below is an example of using the modules together:

```python
from modules.record import Record
from modules.calculator import Calculator
from modules.calories_calculator import CaloriesCalculator
from modules.cash_calculator import CashCalculator

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

-   **record.py**: Stores records with amount (money or calories), date, and comment. Validates inputs and handles date parsing.
-   **calculator.py**: Base class for tracking records with methods for adding records and calculating daily/weekly stats.
-   **calories_calculator.py**: Extends `Calculator` for calorie tracking with limits and user-friendly messages.
-   **cash_calculator.py**: Extends `Calculator` for cash spending with currency conversion (USD, EUR, RUB).

## Notes

-   This directory is part of a larger project structure that may include directories like `tests` for unit tests or other components.
-   Ensure all modules are in the same directory for proper imports.
-   Refer to individual module docstrings for detailed API information.
