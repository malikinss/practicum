# CashCalculator Module

## Overview

The `CashCalculator` module provides a Python class, `CashCalculator`, for tracking daily cash spending with support for currency conversion.

It inherits from the `Calculator` class to manage spending records and extends it with functionality to convert and display remaining cash in USD, EUR, or RUB.

The module is designed for applications requiring currency-aware budget tracking.

## Features

-   Track daily cash spending with a limit in RUB.
-   Support currency conversion for USD, EUR, and RUB using fixed exchange rates.
-   Add records while preventing overspending or future-dated entries.
-   Provide user-friendly messages about remaining cash or debt in the specified currency.
-   Enforce strict validation for inputs and currency codes.

## Installation

The `CashCalculator` module requires Python 3.8 or higher and depends on the `Calculator` and `Record` modules. Copy `record.py`, `calculator.py`, and `cash_calculator.py` into your project directory.

```bash
# No pip install required; ensure record.py and calculator.py are in the same directory
```

### Dependencies

-   Python standard library: `datetime` (via `Calculator` and `Record`)
-   `typing` (via `Calculator` for type hints)
-   `Record` module (required by `Calculator`)
-   `Calculator` module (must be in the same directory as `cash_calculator.py`)

## Usage

The `CashCalculator` class can be used to track cash spending with a daily limit and view remaining amounts in different currencies. Below is an example:

```python
from record import Record
from cash_calculator import CashCalculator

# Initialize a cash calculator with a daily limit of 10000 RUB
calc = CashCalculator(limit=10000)

# Create and add a record
record = Record(amount=5000, date="2025-05-24", comment="Groceries")
calc.add_record(record)

# Get remaining cash in USD
print(calc.get_today_cash_remained("USD"))
# Output: You have 63.02 USD left for today

# Get remaining cash in EUR
print(calc.get_today_cash_remained("EUR"))
# Output: You have 55.43 EUR left for today
```

### Error Handling

The module includes strict validation:

```python
from record import Record
from cash_calculator import CashCalculator

calc = CashCalculator(limit=10000)

# Invalid currency type
try:
    calc.get_today_cash_remained(123)  # Raises TypeError
except TypeError as e:
    print(e)  # Output: Currency must be a string

# Unsupported currency
try:
    calc.get_today_cash_remained("GBP")  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Unsupported currency

# Exceeding daily limit
try:
    record = Record(amount=12000, date="2025-05-24", comment="Overspend")
    calc.add_record(record)  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Record amount exceeds today's limit
```

## API Reference

### `CashCalculator` Class

-   `CashCalculator(limit: int)`

    -   **Purpose**: Initialize a cash calculator with a daily spending limit in RUB.
    -   **Parameters**:
        -   `limit`: `int` - Daily spending limit in RUB.
    -   **Raises**:
        -   `ValueError`: If `limit` is not an integer or is negative (via `Calculator`).
    -   **Returns**: None

-   `add_record(record: Record) -> None`

    -   **Purpose**: Add a `Record` object if it meets the daily limit and date constraints.
    -   **Parameters**:
        -   `record`: `Record` - A `Record` instance to add.
    -   **Raises**:
        -   `TypeError`: If `record` is not a `Record` instance.
        -   `ValueError`: If `record.date` is in the future or `record.amount` exceeds the remaining daily limit.
    -   **Returns**: None

-   `get_today_cash_remained(currency: str) -> str`

    -   **Purpose**: Return a message about remaining cash for today in the specified currency.
    -   **Parameters**:
        -   `currency`: `str` - Currency code (USD, EUR, or RUB).
    -   **Raises**:
        -   `TypeError`: If `currency` is not a string.
        -   `ValueError`: If `currency` is empty or unsupported.
    -   **Returns**: `str` - Message indicating remaining cash or debt.

-   `_get_cash_message(remained: float, currency: str) -> str`

    -   **Purpose**: Format a message based on remaining cash in the specified currency.
    -   **Parameters**:
        -   `remained`: `float` - Remaining amount in the specified currency.
        -   `currency`: `str` - Currency code.
    -   **Returns**: `str` - Message like “You have X.XX <currency> left for today” or “No money left, hold on: your debt is X.XX <currency>”.
    -   **Note**: Internal method.

-   `_convert_to_rate(amount: int, currency: str) -> float`
    -   **Purpose**: Convert an amount from RUB to the specified currency.
    -   **Parameters**:
        -   `amount`: `int` - Amount in RUB.
        -   `currency`: `str` - Target currency (USD, EUR, or RUB).
    -   **Raises**:
        -   `ValueError`: If `currency` is unsupported.
    -   **Returns**: `float` - Converted amount.
    -   **Note**: Internal method.

### Inherited Methods

The `CashCalculator` class inherits all methods from the `Calculator` class, including:

-   `get_today_stats() -> str`: Return today’s spending and remaining budget in RUB.
-   `get_week_stats() -> str`: Return total spending over the last 7 days in RUB.
-   See the `Calculator` module documentation for details.

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

For issues or questions, please open an issue on the [GitHub repository](https://github.com/username/cash-calculator-module) or contact the maintainer.
