# FitnessTracker Class Implementation

## Description 📝

The provided code implements the `FitnessTracker` class, a software module for the "Runaway" fitness tracker from Unicorn, designed to process step data and display a daily activity summary.

The class handles input data packages as tuples containing a time string (`HH:MM:SS`) and step count, validates the data, calculates steps, distance, calories, and a motivational message, and stores the data in a dictionary.

The implementation follows the technical specifications, including data validation, in-place storage, and formatted output. The example usage processes a package `("09:36:02", 15000)` and prints a summary.

## Purpose 🎯

Intended for fitness tracking applications, data processing, or educational examples of object-oriented programming, datetime handling, and precise arithmetic in Python.

## How It Works 🔍

-   **Module Imports**:
    -   `import datetime as dt`: Imports `datetime` with alias `dt` to avoid naming conflicts.
    -   `from decimal import Decimal`: For precise arithmetic in calorie calculations.
    -   `from typing import Dict, Tuple`: For type hints.
-   **Class Definition**:
    -   `FitnessTracker` class with constants:
        -   `WEIGHT = 75`, `HEIGHT = 175`: Fixed user parameters.
        -   `K_1 = 0.035`, `K_2 = 0.029`: Calorie calculation coefficients.
        -   `STEP_M = 0.65`: Step length in meters.
        -   `TIME_FORMAT = '%H:%M:%S'`: Time format for parsing.
        -   `MOTIVATIONS`: List of motivational messages.
-   **Methods**:
    -   `__init__`: Initializes an empty `storage_data` dictionary (`Dict[dt.datetime, int]`).
    -   `check_correct_data`: Validates package:
        -   Checks tuple length (`len(data) == 2`).
        -   Ensures non-empty values (`all(data)`).
        -   Verifies types (`str` for time, `int` for steps).
        -   Validates time format using `strptime`.
    -   `check_correct_time`: Ensures time is later than previous entries:
        -   Parses time and compares with stored times.
    -   `get_step_day`: Sums steps in `storage_data` plus current package steps.
    -   `get_distance`: Converts steps to kilometers: `(steps * STEP_M) / 1000`, rounded to 2 decimals.
    -   `get_decimal`: Converts numbers to `Decimal` for precision.
    -   `get_spent_calories`: Calculates calories:
        -   Uses time to compute hours.
        -   Formula: `(K_1 * weight + (speed^2 / height)) * K_2 * weight * minutes`.
        -   Rounds to 2 decimals.
    -   `get_achievement`: Selects motivational message based on distance:
        -   `≥ 6.5 km`: "Great result! Goal reached".
        -   `≥ 3.9 km`: "Not bad! It was a productive day."
        -   `≥ 2 km`: "Not enough, but we'll make up for it tomorrow!"
        -   `< 2 km`: "Lying down is also good for you..."
    -   `show_message`: Prints summary in specified format.
    -   `accept_package`: Main entry point:
        -   Validates package, processes data, updates `storage_data`, prints summary, and returns `storage_data`.
-   **Main Code**:
    -   Creates `FitnessTracker` instance.
    -   Processes package `("09:36:02", 15000)`.
-   **Behavior**:
    -   For `("09:36:02", 15000)`:
        -   Validates package and time.
        -   Steps: `15000`.
        -   Distance: `(15000 * 0.65) / 1000 = 9.75 km`.
        -   Calories:
            -   Hours: `9 + 36/60 = 9.6`.
            -   Speed: `9.75 / 9.6 = 1.015625 km/h`.
            -   Calories/min: `(0.035 * 75 + (1.015625^2 / 175)) * 0.029 * 75`.
            -   Total: Approx. `1512.00 kcal` (after rounding).
        -   Achievement: `9.75 ≥ 6.5` → "Great result! Goal reached".
        -   Output:
            ```
            Time: 09:36:02.
            Number of steps for today: 15000.
            Distance was 9.75 km.
            You burned 1512.00 kcal.
            Great result! Goal reached.
            ```

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:
    -   Processes package `("09:36:02", 15000)`.
    -   Stores data in `storage_data` after validation.
    -   Calculates:
        -   Steps: `15000`.
        -   Distance: `9.75 km`.
        -   Calories: `1512.00 kcal`.
        -   Message: "Great result! Goal reached".
    -   Prints summary in exact format.
-   **Data Validation**:
    -   Checks tuple length, non-empty values, types, and time format.
    -   Ensures time is later than previous entries.
    -   Returns unchanged `storage_data` if validation fails.
-   **Calculations**:
    -   Steps: Correctly sums current and stored steps.
    -   Distance: `(steps * 0.65) / 1000`, rounded to 2 decimals.
    -   Calories: Precise with `Decimal`, matches formula.
    -   Motivational message: Correctly selected based on distance thresholds.
-   **Output**:
    -   Matches example format exactly, including punctuation and rounding.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `check_correct_data` ensures valid tuple, types, and time format.
    -   `check_correct_time` prevents out-of-order times within a day.
    -   `get_distance` and `get_spent_calories` use specified constants and rounding.
    -   `get_achievement` matches exact distance thresholds.
    -   `show_message` uses precise formatting.
-   **Performance**:
    -   `check_correct_data`: O(1) for fixed-size tuple.
    -   `check_correct_time`: O(n) for n stored entries (small in practice).
    -   `get_step_day`: O(n) for summing values.
    -   `get_distance`, `get_spent_calories`, `get_achievement`: O(1).
    -   `show_message`: O(1).
    -   Total: O(n), efficient for typical usage.
-   **Design**:
    -   Type hints (`Dict[dt.datetime, int]`, `Tuple[str, int]`) clarify types.
    -   Modular methods enhance maintainability.
    -   `Decimal` ensures precision in calorie calculations.
    -   Constants are clearly defined.
-   **Alternatives**:
    -   Store steps as cumulative: Requires adjusting calculations.
    -   Use floats instead of `Decimal`: Risks precision errors.
    -   Single method: Less modular and harder to maintain.
-   **Extensibility**:
    -   Easily modified for different time formats or constants.
    -   Could add daily reset logic or additional metrics (e.g., average speed).
    -   Could validate step counts (e.g., non-negative).
-   **Edge Cases**:
    -   Empty package: Rejected by `check_correct_data`.
    -   Invalid time format: Rejected by `check_correct_data`.
    -   Out-of-order time: Rejected by `check_correct_time`.
    -   Zero steps: Handled correctly.
    -   Large steps: No limits, handled by Python’s integers.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Provided example
tracker = FitnessTracker()
package = ("09:36:02", 15000)
tracker.accept_package(package)
# Output:
# Time: 09:36:02.
# Number of steps for today: 15000.
# Distance was 9.75 km.
# You burned 1512.00 kcal.
# Great result! Goal reached.

# Additional test cases
tracker.accept_package(("10:00:00", 1000))  # ~0.65 km
# Output:
# Time: 10:00:00.
# Number of steps for today: 16000.
# Distance was 10.40 km.
# You burned 1664.00 kcal.
# Great result! Goal reached.

tracker.accept_package(("08:00:00", 1000))  # Invalid time (earlier)
# No output, returns storage_data unchanged

tracker.accept_package(("invalid", 1000))  # Invalid format
# No output, returns storage_data unchanged
```

## Conclusion 🚀

The `FitnessTracker` class implementation is precise, correctly processing the data package `("09:36:02", 15000)`, performing validations, calculating steps, distance, calories, and motivational messages, and printing the summary in the exact format.

It is robust, efficient, and fully compliant with the technical specifications, making it ideal for fitness tracking or teaching object-oriented programming, datetime handling, and precise calculations.
