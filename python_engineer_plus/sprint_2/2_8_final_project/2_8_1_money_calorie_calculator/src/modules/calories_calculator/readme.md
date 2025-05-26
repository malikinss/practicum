# CaloriesCalculator Module

## Overview

The `CaloriesCalculator` module provides a Python class, `CaloriesCalculator`, for tracking daily calorie intake with a specified limit.

It inherits from the `Calculator` class to manage spending records and extends it with calorie-specific functionality, such as formatting messages based on remaining calories.

The module is designed for applications focused on dietary tracking and calorie management.

## Features

-   Track daily calorie intake with a limit between 1000 and 3000 kcal.
-   Inherit record management and spending calculations from the `Calculator` class.
-   Provide user-friendly messages about remaining daily calories or instructions to stop eating.
-   Enforce strict validation for calorie limits and record inputs.

## Installation

The `CaloriesCalculator` module requires Python 3.8 or higher and depends on the `Calculator` and `Record` modules.
Copy `record.py`, `calculator.py`, and `calories_calculator.py` into your project directory.

```bash
# No pip install required; ensure record.py and calculator.py are in the same directory
```

### Dependencies

-   Python standard library: `datetime` (via `Calculator` and `Record`)
-   `typing` (via `Calculator` for type hints)
-   `Record` module (required by `Calculator`)
-   `Calculator` module (must be in the same directory as `calories_calculator.py`)

## Usage

The `CaloriesCalculator` class can be used to track calorie intake with a daily limit. Below is an example of how to use it:

```python
from record import Record
from calories_calculator import CaloriesCalculator

# Initialize a calorie calculator with a daily limit of 2000 kcal
calc = CaloriesCalculator(limit=2000)

# Create and add a calorie record
record = Record(amount=500, date="2025-05-24", comment="Breakfast")
calc.add_record(record)

# Get remaining calories message
print(calc.get_today_calories_remained())
# Output: Today you can eat something else, but with a total caloric content of no more than 1500 kcal

# Add another record exceeding the limit
try:
    record = Record(amount=1600, date="2025-05-24", comment="Dinner")
    calc.add_record(record)  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Record amount exceeds today's limit
```

### Error Handling

The module includes strict validation:

```python
from calories_calculator import CaloriesCalculator

# Invalid limit
try:
    calc = CaloriesCalculator(limit=500)  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Limit must be between 1000 and 3000 kcal

# Non-integer limit
try:
    calc = CaloriesCalculator(limit=2000.5)  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Limit must be an integer
```

## API Reference

### `CaloriesCalculator` Class

-   `CaloriesCalculator(limit: int)`

    -   **Purpose**: Initialize a calorie calculator with a daily calorie limit.
    -   **Parameters**:
        -   `limit`: `int` - Daily calorie limit (1000–3000 kcal).
    -   **Raises**:
        -   `ValueError`: If `limit` is not an integer or is outside the 1000–3000 kcal range.
    -   **Returns**: None

-   `get_today_calories_remained() -> str`

    -   **Purpose**: Return a message about remaining calories for today.
    -   **Returns**: `str` - Message indicating remaining calories or to stop eating.

-   `_get_calories_message(remained: int) -> str`
    -   **Purpose**: Format a message based on remaining calories.
    -   **Parameters**:
        -   `remained`: `int` - Remaining calories for today.
    -   **Returns**: `str` - Message like “Today you can eat something else, but with a total caloric content of no more than X kcal” or “Stop eating!”.
    -   **Note**: Internal method.

### Inherited Methods

The `CaloriesCalculator` class inherits all methods from the `Calculator` class, including:

-   `add_record(record: Record) -> None`: Add a `Record` object if it meets the daily limit and date constraints.
-   `get_today_stats() -> str`: Return today’s spending and remaining budget.
-   `get_week_stats() -> str`: Return total spending over the last 7 days.
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

For issues or questions, please open an issue on the [GitHub repository](https://github.com/username/calories-calculator-module) or contact the maintainer.
