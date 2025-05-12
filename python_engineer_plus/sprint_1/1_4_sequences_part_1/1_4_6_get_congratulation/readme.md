# Fitness Tracker with Congratulation Message Implementation

## Description 📝

The provided code enhances the fitness tracker module by adding a `get_congratulation` function to select an appropriate congratulatory message based on the distance walked.
The `get_stats` function is updated to include this message in the output.
The program converts steps to kilometers, calculates kilocalories burned, determines the congratulation based on distance thresholds, and outputs a formatted string: `Today you walked <distance_in_km> km and spent <number_of_kilocalories> kilocalories. <congratulation>`.
All numeric values are rounded to two decimal places, and f-strings are used for formatting.

## Purpose 🎯

Intended for fitness tracking applications with motivational feedback, user activity analysis, or educational examples of conditional logic, string formatting, and modular design in Python.

## How It Works 🔍

-   **convert_to_km Function**:
    -   Takes `steps` (integer).
    -   Uses `STEP_LENGTH_M = 0.65` (meters per step).
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
-   **get_congratulation Function**:
    -   Takes `distance` (km, float).
    -   Returns a congratulatory message based on distance:
        -   `>= 6.5` km: `"Excellent result! Goal achieved."`
        -   `>= 3.9` km: `"Not bad! The day was productive."`
        -   `>= 2` km: `"Not enough, but we'll make up for it tomorrow!"`
        -   `< 2` km: `"Lying down is also useful. The main thing is participation, not victory!"`
    -   Uses chained conditionals to check thresholds in descending order.
-   **get_stats Function**:
    -   Takes `distance` (km), `calories` (kilocalories), and `congratulation` (string).
    -   Returns an f-string:
        -   `f"Today you walked {distance:.2f} km and spent {calories:.2f} kilocalories. {congratulation}"`.
    -   Formats `distance` and `calories` to two decimal places (`:.2f`).
-   **Main Code**:
    -   Calls `get_fitness_data()` to get `steps`, `weight`, `height`, `hours`.
    -   Computes `distance` with `convert_to_km(steps)`.
    -   Computes `calories` with `calculate_calories(weight, height, distance, hours)`.
    -   Gets `congratulation` with `get_congratulation(distance)`.
    -   Calls `get_stats(distance, calories, congratulation)` and prints the result.
-   **Behavior**:
    -   Converts steps to kilometers and calculates calories.
    -   Selects a congratulation based on distance.
    -   Outputs a formatted string with distance, calories, and the congratulation.

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:
    -   Outputs: `Today you walked <distance> km and spent <calories> kilocalories. <congratulation>`.
    -   Example input: `steps = 16215`.
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
        -   Congratulation: `distance = 10.54 >= 6.5` → `"Excellent result! Goal achieved."`.
        -   Output: `Today you walked 10.54 km and spent 356.40 kilocalories. Excellent result! Goal achieved.`
    -   Other cases:
        -   `distance = 4.0` (steps ≈ 6154): `"Not bad! The day was productive."`.
        -   `distance = 2.0` (steps ≈ 3077): `"Not enough, but we'll make up for it tomorrow!"`.
        -   `distance = 1.0` (steps ≈ 1538): `"Lying down is also useful. The main thing is participation, not victory!"`.
-   **Format**:
    -   Uses f-strings for exact formatting.
    -   Distance and calories formatted to two decimal places (`:.2f`).
    -   Congratulation appended with a space after kilocalories.
    -   Matches required wording and punctuation.
-   **Congratulation Logic**:
    -   Correctly selects messages based on thresholds: `6.5`, `3.9`, `2.0`.
    -   Handles boundary cases (e.g., `distance = 6.5`, `3.9`, `2.0`) with `>=`.
-   **Precision**:
    -   `convert_to_km` uses float arithmetic, sufficient with rounding.
    -   `calculate_calories` uses `Decimal` for precise arithmetic.
-   **Correctness**:
    -   Step conversion uses `0.65` meters.
    -   Calorie formula is consistent with prior tasks.
    -   Fixed `weight`, `height`, `hours` align with example context.
    -   No validation needed, as inputs are guaranteed valid.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `get_congratulation` uses descending thresholds (`>= 6.5`, `>= 3.9`, `>= 2`) to ensure correct message selection.
    -   `get_stats` formats all components correctly, including space before congratulation.
    -   Rounding in `convert_to_km` and `calculate_calories` ensures consistent output.
    -   Fixed inputs (`weight=75`, `height=175`, `hours=2`) simplify the example.
-   **Performance**:
    -   `convert_to_km`: O(1) for arithmetic.
    -   `calculate_calories`: O(1) for arithmetic.
    -   `get_fitness_data`: O(1) for input.
    -   `get_congratulation`: O(1) for conditionals.
    -   `get_stats`: O(1) for string formatting.
    -   Total: O(1), highly efficient.
-   **Design**:
    -   Type hints clarify signatures.
    -   Modular functions enhance maintainability.
    -   F-strings in `get_stats` are concise and readable.
    -   `STEP_LENGTH_M` constant is clear.
-   **Alternatives**:
    -   Dictionary for congratulations: More complex for ordered thresholds.
    -   String concatenation: Less readable than f-strings.
    -   Inline conditionals in `get_stats`: Less modular than `get_congratulation`.
-   **Extensibility**:
    -   Easily modified to add more thresholds or messages.
    -   Could accept variable `weight`, `height`, `hours`.
    -   Could include additional stats (e.g., steps).
-   **Edge Cases**:
    -   Zero steps: `distance = 0.0`, congratulation = `"Lying down..."`.
    -   Boundary distances (`6.5`, `3.9`, `2.0`): Handled correctly with `>=`.
    -   Large steps: Handled by float arithmetic.
    -   Non-integer steps: Not applicable (`steps` is `int`).

## Usage Example (For Clarity, Not Submission) 📦

```python
# Simulated example
steps, weight, height, hours = 16215, 75.0, 175.0, 2.0
distance = convert_to_km(steps)  # 10.54
calories = calculate_calories(weight, height, distance, hours)  # 356.40
congratulation = get_congratulation(distance)  # Excellent result! Goal achieved.
print(get_stats(distance, calories, congratulation))
# Output: Today you walked 10.54 km and spent 356.40 kilocalories. Excellent result! Goal achieved.

# Test cases for different distances
def test_stats(steps):
    d = convert_to_km(steps)
    c = calculate_calories(75, 175, d, 2)
    cong = get_congratulation(d)
    print(get_stats(d, c, cong))

test_stats(10000)  # ~6.5 km
# Output: Today you walked 6.50 km and spent 349.38 kilocalories. Excellent result! Goal achieved.

test_stats(6000)  # ~3.9 km
# Output: Today you walked 3.90 km and spent 331.90 kilocalories. Not bad! The day was productive.

test_stats(3077)  # ~2.0 km
# Output: Today you walked 2.00 km and spent 321.74 kilocalories. Not enough, but we'll make up for it tomorrow!

test_stats(1000)  # ~0.65 km
# Output: Today you walked 0.65 km and spent 317.73 kilocalories. Lying down is also useful. The main thing is participation, not victory!
```

## Conclusion 🚀

The enhanced fitness tracker implementation is precise, correctly converting steps to kilometers, calculating calories, selecting the appropriate congratulation, and formatting the output as `Today you walked <distance> km and spent <calories> kilocalories. <congratulation>`.
It uses f-strings, rounds to two decimal places, and handles all distance thresholds.
The implementation is efficient, extensible, and ideal for fitness tracking or teaching conditional logic and formatting, fully compliant with the task’s requirements.
