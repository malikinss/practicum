# Calculator Module

## Overview

The `Calculator` module provides a Python class, `Calculator`, for tracking spending records with a daily budget limit.

It allows users to add spending records, check today’s spending, and calculate the remaining budget for today and the total spent over the last 7 days.

The module integrates with the `Record` class to store individual spending records with attributes for amount, date, and comment.

## Features

-   Track spending with a configurable daily limit.
-   Add records while ensuring they don’t exceed the daily limit or have future dates.
-   Calculate total spending for today and the remaining daily budget.
-   Summarize total spending over the last 7 days.
-   Robust input validation to ensure correct data types and constraints.

## Installation

The `Calculator` module requires Python 3.8 or higher and depends on the `Record` module. Copy both `Record.py` and `Calculator.py` into your project directory.

```bash
# No pip install required; ensure record.py is in the same directory
```

### Dependencies

-   Python standard library: `datetime`
-   `typing` (for type hints)
-   `Record` module (must be in the same directory as `Calculator.py`)

## Usage

The `Calculator` class can be used to manage spending records with a daily limit. Below is an example of how to use it:

```python
from record import Record
from calculator import Calculator

# Initialize a calculator with a daily limit of 100
calc = Calculator(limit=100)

# Create and add a record
record = Record(amount=50, date="2025-05-24", comment="Lunch")
calc.add_record(record)

# Get today's statistics
print(calc.get_today_stats())  # Output: Today: spent 50, remained 50

# Get last 7 days' statistics
print(calc.get_week_stats())  # Output: Last 7 days: spent 50
```

### Error Handling

The module enforces strict validation:

```python
from record import Record
from calculator import Calculator

calc = Calculator(limit=100)

# Invalid record type
try:
    calc.add_record("invalid")  # Raises TypeError
except TypeError as e:
    print(e)  # Output: Record must be an instance of Record

# Future date
try:
    record = Record(amount=20, date="2025-06-01", comment="Future")
    calc.add_record(record)  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Record date cannot be in the future

# Exceeding daily limit
try:
    record = Record(amount=150, date="2025-05-24", comment="Overspend")
    calc.add_record(record)  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Record amount exceeds today's limit
```

## API Reference

### `Calculator` Class

-   `Calculator(limit: int)`

    -   **Purpose**: Initialize a calculator with a daily spending limit.
    -   **Parameters**:
        -   `limit`: `int` - Non-negative integer representing the daily spending limit.
    -   **Raises**:
        -   `ValueError`: If `limit` is not an integer or is negative.
    -   **Returns**: None

-   `add_record(record: Record) -> None`

    -   **Purpose**: Add a `Record` object if it meets the daily limit and date constraints.
    -   **Parameters**:
        -   `record`: `Record` - A `Record` instance to add.
    -   **Raises**:
        -   `TypeError`: If `record` is not a `Record` instance.
        -   `ValueError`: If `record.date` is in the future or `record.amount` exceeds the remaining daily limit.
    -   **Returns**: None

-   `_get_spent_by_date(date: datetime.date) -> int`

    -   **Purpose**: Calculate total amount spent on a specific date.
    -   **Parameters**:
        -   `date`: `datetime.date` - Date to check.
    -   **Returns**: `int` - Total amount spent on the given date.
    -   **Note**: Internal method.

-   `_get_today_spent() -> int`

    -   **Purpose**: Calculate total amount spent today.
    -   **Returns**: `int` - Total amount spent today.
    -   **Note**: Internal method.

-   `_get_today_remained() -> int`

    -   **Purpose**: Calculate remaining budget for today.
    -   **Returns**: `int` - Remaining amount for today’s budget.
    -   **Note**: Internal method.

-   `get_today_stats() -> str`

    -   **Purpose**: Return a string with today’s spending and remaining budget.
    -   **Returns**: `str` - Format: `Today: spent <amount>, remained <amount>`.

-   `get_week_stats() -> str`

    -   **Purpose**: Return a string with total spending over the last 7 days.
    -   **Returns**: `str` - Format: `Last 7 days: spent <amount>`.

-   `_get_week_dates() -> List[datetime.date]`
    -   **Purpose**: Get a list of dates for today and the previous 6 days.
    -   **Returns**: `List[datetime.date]` - List of the last 7 days’ dates.
    -   **Note**: Internal method.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For issues or questions, please open an issue on the [GitHub repository](https://github.com/username/calculator-module) or contact the maintainer.
