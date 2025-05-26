# Budget and Calorie Tracker

## Overview

The Budget and Calorie Tracker is a Python-based application designed to track daily financial spending and calorie intake.

It provides two specialized calculators: `CashCalculator` for managing monetary expenses with currency conversion (RUB, USD, EUR) and `CaloriesCalculator` for monitoring calorie consumption.

Both inherit from a base `Calculator` class, which handles record management and statistics.

The project is structured to ensure modularity, maintainability, and adherence to PEP 8 standards. Type hints are included for clarity, though optional per the project requirements.

## Project Structure

-   `src/`: Contains the core implementation in a `modules` subdirectory.
    -   `modules/record/`: Contains `record.py`, defining the `Record` class for storing records with amount, date, and comment.
    -   `modules/calculator/`: Contains `calculator.py`, defining the base `Calculator` class for tracking records with a daily limit.
    -   `modules/calories_calculator/`: Contains `calories_calculator.py`, extending `Calculator` for calorie tracking with specific limits and messaging.
    -   `modules/cash_calculator/`: Contains `cash_calculator.py`, extending `Calculator` for cash spending with currency conversion.
-   `tests/`: Contains test files for unit testing (not detailed here).
-   `homework.py`: Main script for running the application, importing modules from `src/modules`.

## Features

-   Store records with amount (money or calories), date, and comment attributes.
-   Track daily financial spending with customizable limits in RUB.
-   Track daily calorie intake with limits between 1000 and 3000 kcal and user-friendly messages.
-   Support cash tracking with conversion between RUB, USD, and EUR using fixed exchange rates (e.g., USD: 79.34, EUR: 90.2).
-   Provide daily and weekly statistics for financial and calorie tracking.
-   Enforce robust input validation for amounts, dates, limits, and currencies.
-   Adhere to PEP 8 standards for code style and readability.

## Requirements

-   Python 3.8 or higher.
-   No external dependencies beyond the Python standard library (`datetime`, `typing`).
-   All module files (`record.py`, `calculator.py`, `calories_calculator.py`, `cash_calculator.py`) must be in their respective subdirectories under `src/modules`.

## Installation

Clone the repository and ensure the `src/modules` directory is in your project path:

```bash
git clone https://github.com/username/hw_python_oop.git
cd hw_python_oop
```

No external packages are required; copy the `src` directory to your project.

## Usage

The application can be used via the `homework.py` script or by importing modules directly. Below is an example from `homework.py` demonstrating both calculators:

```python
from src.modules.record.record import Record
from src.modules.calculator.calculator import Calculator
from src.modules.calories_calculator.calories_calculator import CaloriesCalculator
from src.modules.cash_calculator.cash_calculator import CashCalculator

# Create a record
record = Record(amount=145, comment="Coffee", date="08.03.2019")

# Cash tracking
cash_calculator = CashCalculator(limit=1000)
cash_calculator.add_record(record)
print(cash_calculator.get_today_cash_remained("rub"))
# Output: На сегодня осталось 855 руб

# Calorie tracking
calorie_calculator = CaloriesCalculator(limit=2000)
calorie_calculator.add_record(Record(amount=1186, comment="Cake", date="24.02.2019"))
print(calorie_calculator.get_today_calories_remained())
# Output: Today you can eat something else, but with a total caloric content of no more than 814 kcal
```

### Error Handling

The modules enforce strict validation:

```python
from src.modules.record.record import Record
from src.modules.cash_calculator.cash_calculator import CashCalculator

# Invalid currency
cash_calc = CashCalculator(limit=1000)
try:
    cash_calc.get_today_cash_remained("gbp")  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Unsupported currency

# Invalid calorie limit
from src.modules.calories_calculator.calories_calculator import CaloriesCalculator
try:
    calorie_calc = CaloriesCalculator(limit=500)  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Limit must be between 1000 and 3000 kcal
```

## Module Details

-   **modules/record/record.py**: Defines `Record` class for storing records with amount (money or calories), date (defaulting to today), and comment. Validates inputs and handles date parsing in `%d.%m.%Y` format.
-   **modules/calculator/calculator.py**: Base class for tracking records with a daily limit. Includes methods for adding records (`add_record`), daily stats (`get_today_stats`), and weekly stats (`get_week_stats`).
-   **modules/calories_calculator/calories_calculator.py**: Extends `Calculator` for calorie tracking with limits (1000–3000 kcal). Provides `get_calories_remained` for user-friendly messages.
-   **modules/cash_calculator/cash_calculator.py**: Extends `Calculator` for cash spending with currency conversion (RUB, USD, EUR). Provides `get_today_cash_remained` for remaining cash or debt messages.

## Development Guidelines

-   **Code Style**: The project adheres to PEP 8 standards. Run the following to check compliance:
    ```bash
    flake8 src/modules/*/homework.py
    ```
-   **Testing**: Unit tests are located in the `tests` directory. Run tests with:
    ````Magnets:
      ```bash
      pytest
    ````
    Ensure all tests pass.
-   **Type Hints**: Included for clarity but optional per project requirements.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository (`https://github.com/username/hw_python_oop`).
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For issues or questions, please open an issue on the [GitHub repository](https://github.com/username/hw_python_oop) or contact the maintainer.
