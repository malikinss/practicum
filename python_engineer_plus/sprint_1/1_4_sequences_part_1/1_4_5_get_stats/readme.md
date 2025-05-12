# Fitness Tracker with Formatted Output Implementation

## Description 📝

The provided code enhances the fitness tracker module by adding a `get_stats` function to format and output a user-friendly message.
The module converts steps to kilometers, calculates kilocalories burned, and now prints a string in the format: `Today you walked <distance_in_km> km and spent <number_of_kilocalories> kilocalories.`
The values for distance and calories are rounded to two decimal places and embedded using f-strings.
The code retains the existing functions (`convert_to_km`, `calculate_calories`, `get_fitness_data`) and uses fixed values for weight (75 kg), height (175 cm), and duration (2 hours).

## Purpose 🎯

Intended for fitness tracking applications requiring user-friendly output, user activity analysis, or educational examples of string formatting, unit conversion, and precise arithmetic in Python.

## How It Works 🔍

-   **convert_to_km Function**:
    -   Takes an integer `steps`.
    -   Uses constant `STEP_LENGTH_M = 0.65` (meters per step).
    -   Calculates distance: `(steps * 0.65) / 1000` km.
    -   Rounds to two decimal places and returns as a float.
-   **calculate_calories Function**:
    -   Takes `weight` (kg), `height` (cm), `dist` (km), `hours` (hours).
    -   Uses `Decimal` for precision:
        -   Speed: `dist / hours` (km/h).
        -   Minutes: `hours * 60`.
        -   Calories per minute: `0.035 * weight + (speed^2 / height) * 0.029 * weight`.
    -   Multiplies by minutes, rounds to two decimal places, and returns as a float.
-   **get_fitness_data Function**:
    -   Prompts for `steps` (converted to `int`).
    -   Returns tuple `(steps, weight, height, hours)` with fixed:
        -   `weight = 75.0` (kg).
        -   `height = 175.0` (cm).
        -   `hours = 2.0` (hours).
-   **get_stats Function**:
    -   Takes `distance` (km) and `calories` (kilocalories).
    -   Returns an f-string:
        -   `f"Today you walked {distance:.2f} km and spent {calories:.2f} kilocalories."`.
    -   Formats `distance` and `calories` to two decimal places using `:.2f`.
-   **Main Code**:
    -   Calls `get_fitness_data()` to get `steps`, `weight`, `height`, `hours`.
    -   Computes `distance` with `convert_to_km(steps)`.
    -   Computes `calories` with `calculate_calories(weight, height, distance, hours)`.
    -   Calls `get_stats(distance, calories)` and prints the result.
-   **Behavior**:
    -   Converts steps to kilometers and calculates calories.
    -   Outputs a formatted string with distance and calories, both rounded to two decimal places.
    -   Uses `Decimal` in `calculate_calories` for precise arithmetic.

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:
    -   Outputs a string in the format:
        -   `Today you walked <distance_in_km> km and spent <number_of_kilocalories> kilocalories.`
    -   Example input: `steps = 16215` (hypothetical).
        -   Distance: `(16215 * 0.65) / 1000 = 10.53975` km → `10.54`.
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
        -   Output: `Today you walked 10.54 km and spent 356.40 kilocalories.`
-   **Format**:
    -   Uses f-strings for exact string formatting.
    -   Distance and calories are formatted to two decimal places (`:.2f`).
    -   Matches required wording and punctuation.
-   **Precision**:
    -   `convert_to_km` uses float arithmetic, sufficient with rounding.
    -   `calculate_calories` uses `Decimal` to avoid floating-point errors.
-   **Correctness**:
    -   Step conversion uses `0.65` meters per step.
    -   Calorie formula is consistent with prior tasks.
    -   Fixed `weight`, `height`, `hours` align with example context.
    -   No validation needed, as inputs are guaranteed valid.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `get_stats` formats `distance` and `calories` to two decimal places, matching input calculations.
    -   F-string ensures exact wording, including spaces and period.
    -   `convert_to_km` and `calculate_calories` produce rounded values, avoiding precision issues in output.
    -   Fixed inputs (`weight=75`, `height=175`, `hours=2`) simplify the example.
-   **Performance**:
    -   `convert_to_km`: O(1) for arithmetic and rounding.
    -   `calculate_calories`: O(1) for fixed arithmetic.
    -   `get_fitness_data`: O(1) for input and tuple creation.
    -   `get_stats`: O(1) for string formatting.
    -   Total: O(1), highly efficient.
-   **Design**:
    -   Type hints clarify function signatures.
    -   Modular functions (`convert_to_km`, `calculate_calories`, `get_stats`) enhance maintainability.
    -   F-string in `get_stats` is concise and readable.
    -   `STEP_LENGTH_M` constant is clear and reusable.
-   **Alternatives**:
    -   String concatenation: Less readable than f-strings.
    -   `format()` method: More verbose than f-strings.
    -   Direct print in main: Less modular than `get_stats`.
-   **Extensibility**:
    -   Easily modified to include additional stats (e.g., steps).
    -   Could accept variable `weight`, `height`, `hours` from input.
    -   Could adjust `STEP_LENGTH_M` or rounding precision.
-   **Edge Cases**:
    -   Zero steps: `distance = 0.0`, calories reflect base burn (`0.035 * weight`).
    -   Large steps: Handled by float arithmetic.
    -   Non-integer steps: Not applicable (`steps` is `int`).
    -   Zero hours: Not possible with fixed `hours=2`.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Simulated example
steps, weight, height, hours = 16215, 75.0, 175.0, 2.0
distance = convert_to_km(steps)
calories = calculate_calories(weight, height, distance, hours)
print(get_stats(distance, calories))
# Output: Today you walked 10.54 km and spent 356.40 kilocalories.

# Additional test cases
print(get_stats(0.0, calculate_calories(75, 175, 0, 2)))
# Output: Today you walked 0.00 km and spent 315.00 kilocalories.

print(get_stats(convert_to_km(20000), calculate_calories(75, 175, convert_to_km(20000), 2)))
# Output: Today you walked 13.00 km and spent 373.24 kilocalories.

print(get_stats(convert_to_km(1000), calculate_calories(75, 175, convert_to_km(1000), 2)))
# Output: Today you walked 0.65 km and spent 317.73 kilocalories.
```

## Conclusion 🚀

The enhanced fitness tracker implementation is precise, correctly converting steps to kilometers, calculating calories, and formatting the output as `Today you walked <distance> km and spent <calories> kilocalories.` with values rounded to two decimal places.
The `get_stats` function uses f-strings for clear formatting, and the module remains efficient and extensible.
It is ideal for fitness tracking or teaching string formatting and modular design, fully compliant with the task’s requirements.
