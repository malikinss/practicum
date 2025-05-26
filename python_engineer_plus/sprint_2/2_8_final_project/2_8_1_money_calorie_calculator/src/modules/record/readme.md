# Record Module

## Overview

The `Record` module provides a Python class, `Record`, for storing and managing records with attributes for an amount, date, and comment. It includes robust date parsing and string representation methods, making it suitable for applications needing structured record-keeping, such as financial tracking or logging.

## Features

-   Store records with a non-negative integer amount, a date (in YYYY-MM-DD format or defaulting to today), and an optional comment.
-   Validate inputs to ensure amount is a non-negative integer and comment is non-empty.
-   Parse and format dates reliably, defaulting to the current date if invalid or empty input is provided.
-   Provide readable string representations for easy display and debugging.

## Installation

The `Record` module is a standalone Python class requiring no external dependencies beyond the standard library. Ensure you have Python 3.8 or higher installed.

```bash
# No pip install required; copy the module into your project
```

### Dependencies

-   Python standard library: `datetime`

## Usage

The `Record` class can be used to create and manage records. Below is an example of how to use it:

```python
from record import Record

# Create a record with a specific date and comment
record = Record(amount=100, date="2025-05-24", comment="Grocery purchase")
print(record)  # Output: 100 on 2025-05-24 - Grocery purchase

# Create a record with default date (today) and comment
record2 = Record(amount=50)
print(record2)  # Output: 50 on [today's date] - No comment

# Access detailed representation for debugging
print(repr(record))  # Output: Record(amount=100, date=2025-05-24, comment=Grocery purchase)
```

### Error Handling

The module includes input validation:

```python
try:
    invalid_record = Record(amount=-10, comment="Invalid")  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Amount cannot be negative

try:
    empty_comment = Record(amount=20, comment="")  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Comment cannot be empty
```

## API Reference

### `Record` Class

-   `Record(amount: int, date: str = '', comment: str = 'No comment')`

    -   **Purpose**: Initialize a record with amount, date, and comment.
    -   **Parameters**:
        -   `amount`: `int` - Non-negative integer representing the record amount.
        -   `date`: `str` - Date in YYYY-MM-DD format; defaults to today’s date if empty or invalid.
        -   `comment`: `str` - Optional comment; defaults to "No comment" if not provided.
    -   **Raises**:
        -   `ValueError`: If `amount` is not an integer, is negative, or `comment` is empty.
    -   **Returns**: None

-   `_parse_str_to_date(date_str: str) -> datetime.date`

    -   **Purpose**: Parse a date string to a `datetime.date` object.
    -   **Parameters**:
        -   `date_str`: `str` - Date in YYYY-MM-DD format.
    -   **Returns**: `datetime.date` - Parsed date or today’s date if input is invalid/empty.
    -   **Note**: Static method, typically used internally.

-   `_parse_date_to_str(date: datetime.date) -> str`

    -   **Purpose**: Format a `datetime.date` object to a YYYY-MM-DD string.
    -   **Parameters**:
        -   `date`: `datetime.date` - Date object to format.
    -   **Returns**: `str` - Date in YYYY-MM-DD format.
    -   **Note**: Static method, typically used internally.

-   `__str__() -> str`

    -   **Purpose**: Return a readable string representation of the record.
    -   **Returns**: `str` - Format: `<amount> on <date> - <comment>`.

-   `__repr__() -> str`
    -   **Purpose**: Return a detailed string representation for debugging.
    -   **Returns**: `str` - Format: `Record(amount=<amount>, date=<date>, comment=<comment>)`.

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

For issues or questions, please open an issue on the [GitHub repository](https://github.com/username/record-module) or contact the maintainer.
