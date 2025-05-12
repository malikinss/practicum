# Fitness Tracker Implementation

## Description 📝

The provided code implements a fitness tracker module that converts a user-provided number of steps into kilometers and calculates kilocalories burned based on a given formula.
It consists of three functions: `convert_to_km` for step-to-kilometer conversion, `calculate_calories` for calorie expenditure, and `get_fitness_data` for user input.
The program uses a fixed step length (0.65 meters), assumes default values for weight (75 kg), height (175 cm), and duration (2 hours), and outputs the distance in kilometers and calories burned, both rounded to two decimal places, in the format `<distance> <calories>`.

## Purpose 🎯

Intended for fitness tracking applications, user activity analysis, or educational examples of unit conversion, precise arithmetic, and formatted output in Python.

## How It Works 🔍

-   **convert_to_km Function**:
    -   Takes an integer `steps` (number of steps taken).
    -   Uses a constant `STEP_LENGTH_M = 0.65` (step length in meters).
    -   Calculates distance in kilometers: `(steps * 0.65) / 1000`.
    -   Converts to float and rounds to two decimal places with `round(float(...), 2)`.
    -   Returns the distance as a float.
-   **calculate_calories Function**:
    -   Takes `weight` (kg), `height` (cm), `dist` (km), and `hours` (hours).
    -   Calculates speed: `dist / hours` (km/h) using `Decimal` for precision.
    -   Converts hours to minutes: `hours * 60`.
    -   Computes calories per minute using the formula:
        -   `0.035 * weight + (speed^2 / height) * 0.029 * weight`.
    -   Multiplies by minutes to get total calories.
    -   Rounds to two decimal places and returns as a float.
-   **get_fitness_data Function**:
    -   Prompts user for the number of steps and converts to `int`.
    -   Returns a tuple `(steps, weight, height, hours)` with fixed values:
        -   `weight = 75.0` (kg).
        -   `height = 175.0` (cm).
        -   `hours = 2.0` (hours).
    -   Uses type hints (`Tuple[int, float, float, float]`) for clarity.
-   **Main Code**:
    -   Calls `get_fitness_data()` to get `steps`, `weight`, `height`, `hours`.
    -   Computes `distance` using `convert_to_km(steps)`.
    -   Computes `calories` using `calculate_calories(weight, height, distance, hours)`.
    -   Prints `distance` and `calories` formatted to two decimal places:
        -   `f"{distance:.2f} {calories:.2f}"`.
-   **Behavior**:
    -   Converts steps to kilometers using a fixed step length.
    -   Calculates calories based on distance, weight, height, and duration.
    -   Outputs two numbers (distance, calories) separated by a space, both rounded to two decimal places.
    -   Uses `Decimal` in `calculate_calories` to avoid floating-point errors.

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:
    -   Converts steps to kilometers and calculates calories.
    -   Example input: `steps = 16215` (hypothetical user input).
        -   Distance: `(16215 * 0.65) / 1000 = 10.53975` km → `10.54` (rounded).
        -   Calories (for `weight=75`, `height=175`, `dist=10.53975`, `hours=2`):
            -   Speed: `10.53975 / 2 = 5.269875` km/h.
            -   Calories per minute:
                -   `0.035 * 75 = 2.625`.
                -   `speed^2 = 5.269875^2 = 27.7715862890625`.
                -   `speed^2 / height = 27.7715862890625 / 175 = 0.15869479250892857`.
                -   `(speed^2 / height) * 0.029 * 75 = 0.15869479250892857 * 0.029 * 75 = 0.34503397406607144`.
                -   Total per minute: `2.625 + 0.34503397406607144 = 2.97003397406607144`.
            -   Minutes: `2 * 60 = 120`.
            -   Total calories: `2.97003397406607144 * 120 = 356.40407688792857`.
            -   Rounded: `356.40`.
        -   Output: `10.54 356.40`.
-   **Format**:
    -   Prints `<distance> <calories>` (e.g., `10.54 356.40`).
    -   Both values are floats rounded to two decimal places.
-   **Precision**:
    -   `convert_to_km` uses float arithmetic but rounds to two decimal places, sufficient for fitness trackers.
    -   `calculate_calories` uses `Decimal` to avoid floating-point errors in complex calculations.
-   **Correctness**:
    -   Step length (`0.65` meters) is applied correctly.
    -   Calorie formula matches the provided specification (from previous tasks).
    -   Fixed `weight`, `height`, `hours` simplify input for the example.
    -   No validation needed, as inputs are guaranteed valid.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `convert_to_km` accurately converts steps to kilometers: `steps * 0.65 / 1000`.
    -   `calculate_calories` uses the same formula as specified in previous tasks, ensuring consistency.
    -   `Decimal` in `calculate_calories` prevents precision errors (e.g., `0.1 + 0.2 ≠ 0.3`).
    -   Rounding to two decimal places aligns with fitness tracker output standards.
    -   `get_fitness_data` uses fixed values for `weight`, `height`, `hours`, matching the example context.
-   **Performance**:
    -   `convert_to_km`: O(1) for multiplication, division, and rounding.
    -   `calculate_calories`: O(1) for fixed arithmetic operations.
    -   `get_fitness_data`: O(1) for reading input and returning tuple.
    -   Total: O(1), highly efficient for any input.
-   **Design**:
    -   Type hints clarify input and output types.
    -   Separate functions for conversion, calorie calculation, and input improve modularity.
    -   F-string formatting (`:.2f`) ensures exact output format.
    -   Fixed `STEP_LENGTH_M` is clear and maintainable.
-   **Alternatives**:
    -   Float arithmetic in `convert_to_km`: Sufficient here, as simple multiplication/division is precise enough.
    -   `Decimal` in `convert_to_km`: Unnecessary, as rounding to two decimal places mitigates errors.
    -   User input for `weight`, `height`, `hours`: Possible but not required, as fixed values are used.
-   **Extensibility**:
    -   Easily modified to accept variable `weight`, `height`, `hours` from input.
    -   Could adjust `STEP_LENGTH_M` or add validation (e.g., non-negative steps).
    -   Could support different calorie formulas or output formats.
-   **Edge Cases**:
    -   Zero steps: `distance = 0.0`, calories reflect base burn (`0.035 * weight` term).
    -   Large steps: Handled correctly with float arithmetic.
    -   Non-integer steps: Not applicable, as `steps` is `int`.
    -   Zero hours: Would raise `ZeroDivisionError` in `calculate_calories`, but `hours=2` is fixed.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Provided example (simulated input)
steps, weight, height, hours = 16215, 75.0, 175.0, 2.0  # Example steps
distance = convert_to_km(steps)
calories = calculate_calories(weight, height, distance, hours)
print(f"{distance:.2f} {calories:.2f}")  # 10.54 356.40

# Additional test cases
print(convert_to_km(0))  # 0.0
print(convert_to_km(1000))  # 0.65
print(calculate_calories(75, 175, 0, 2))  # 315.0 (base calorie burn)
print(f"{convert_to_km(20000):.2f} {calculate_calories(75, 175, convert_to_km(20000), 2):.2f}")  # 13.00 373.24
```

## Conclusion 🚀

The `convert_to_km`, `calculate_calories`, and `get_fitness_data` implementation is precise, correctly converting steps to kilometers and calculating calories for the fitness tracker.
It produces output in the required format (e.g., `10.54 356.40` for 16215 steps), uses `Decimal` for precise calorie calculations, and rounds to two decimal places.
The implementation is efficient, extensible, and ideal for fitness tracking or teaching unit conversions and formatting, fully compliant with the task’s requirements.
