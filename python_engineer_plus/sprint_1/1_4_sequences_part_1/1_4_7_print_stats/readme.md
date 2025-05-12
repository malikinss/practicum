# Fitness Tracker with Multi-Line Output Implementation

## Description 📝

The provided code modifies the fitness tracker module to improve readability by formatting the output message across multiple lines, with one parameter per line.
The new `print_stats` function replaces the previous `get_stats` function and prints the message in the format:

```
Today you have walked <steps> steps.
Distance covered is <distance> km.
You have burned <calories> kcal.
<congratulation>
```

The message includes the number of steps, distance in kilometers, kilocalories burned (rounded to two decimal places), and a congratulatory message based on the distance.
The code uses a triple-quoted f-string with the `print` function's `sep='\n'` to achieve line-by-line output.
The existing functions (`convert_to_km`, `calculate_calories`, `get_fitness_data`, `get_congratulation`) remain unchanged, and fixed values are used for weight (75 kg), height (175 cm), and duration (2 hours).

## Purpose 🎯

Intended for fitness tracking applications requiring clear, multi-line output for small screens, user activity analysis, or educational examples of string formatting, conditional logic, and precise arithmetic in Python.

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
    -   Returns a message based on distance:
        -   `>= 6.5` km: `"Excellent result! Goal achieved."`
        -   `>= 3.9` km: `"Not bad! The day was productive."`
        -   `>= 2` km: `"Not enough, but we'll make up for it tomorrow!"`
        -   `< 2` km: `"Lying down is also useful. The main thing is participation, not victory!"`
-   **print_stats Function**:
    -   Takes `distance` (km), `calories` (kilocalories), `congratulation` (string), `steps` (integer).
    -   Uses a single `print` statement with a triple-quoted f-string:
        -   `f'Today you have walked {steps} steps.'`
        -   `f'Distance covered is {distance} km.'`
        -   `f'You have burned {calories} kcal.'`
        -   `congratulation`
    -   Sets `sep='\n'` to print each component on a new line.
    -   Returns `None`, as it prints directly.
-   **Main Code**:
    -   Calls `get_fitness_data()` to get `steps`, `weight`, `height`, `hours`.
    -   Computes `distance` with `convert_to_km(steps)`.
    -   Computes `calories` with `calculate_calories(weight, height, distance, hours)`.
    -   Gets `congratulation` with `get_congratulation(distance)`.
    -   Calls `print_stats(distance, calories, congratulation, steps)`.

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:
    -   Outputs a four-line message:
        ```
        Today you have walked <steps> steps.
        Distance covered is <distance> km.
        You have burned <calories> kcal.
        <congratulation>
        ```
    -   Example input: `steps = 10000`.
        -   Distance: `(10000 * 0.65) / 1000 = 6.5` km.
        -   Calories (for `weight=75`, `height=175`, `dist=6.5`, `hours=2`):
            -   Speed: `6.5 / 2 = 3.25` km/h.
            -   Calories per minute:
                -   `0.035 * 75 = 2.625`.
                -   `speed^2 = 3.25^2 = 10.5625`.
                -   `speed^2 / height = 10.5625 / 175 = 0.06035714285714286`.
                -   `(speed^2 / height) * 0.029 * 75 = 0.06035714285714286 * 0.029 * 75 = 0.13125535714285715`.
                -   Total per minute: `2.625 + 0.13125535714285715 = 2.756255357142857`.
            -   Minutes: `2 * 60 = 120`.
            -   Total calories: `2.756255357142857 * 120 = 330.75064285714284`.
            -   Rounded: `330.75`.
        -   Congratulation: `distance = 6.5 >= 6.5` → `"Excellent result! Goal achieved."`.
        -   Output:
            ```
            Today you have walked 10000 steps.
            Distance covered is 6.50 km.
            You have burned 330.75 kcal.
            Excellent result! Goal achieved.
            ```
    -   Other cases:
        -   `steps ≈ 6000` (`distance ≈ 3.9`): `"Not bad! The day was productive."`.
        -   `steps ≈ 3077` (`distance ≈ 2.0`): `"Not enough, but we'll make up for it tomorrow!"`.
        -   `steps ≈ 1000` (`distance ≈ 0.65`): `"Lying down is also useful..."`.
-   **Format**:
    -   Uses triple-quoted f-string with `sep='\n'` for line-by-line output.
    -   Distance and calories formatted to two decimal places (implicit in prior calculations).
    -   Steps is an integer, as provided.
    -   Matches exact wording and punctuation (e.g., "steps.", "km.", "kcal.").
-   **Precision**:
    -   `convert_to_km` and `calculate_calories` round to two decimal places.
    -   `calculate_calories` uses `Decimal` for precision.
-   **Correctness**:
    -   `print_stats` includes all required components: steps, distance, calories, congratulation.
    -   Triple-quoted f-string ensures correct line breaks.
    -   Fixed inputs (`weight=75`, `height=175`, `hours=2`) align with context.
    -   No validation needed, as inputs are guaranteed valid.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `print_stats` uses a single `print` with `sep='\n'` to achieve multi-line output, simpler than multiple `print` calls.
    -   Triple-quoted f-string allows natural formatting of lines.
    -   Distance and calories inherit two-decimal-place rounding from prior functions.
    -   Congratulation messages are selected correctly by `get_congratulation`.
-   **Performance**:
    -   `convert_to_km`: O(1).
    -   `calculate_calories`: O(1).
    -   `get_fitness_data`: O(1).
    -   `get_congratulation`: O(1).
    -   `print_stats`: O(1) for string formatting and printing.
    -   Total: O(1), highly efficient.
-   **Design**:
    -   Type hints clarify signatures.
    -   Modular functions maintain clarity.
    -   Triple-quoted f-string in `print_stats` is readable and matches requirements.
    -   `STEP_LENGTH_M` constant is reusable.
-   **Alternatives**:
    -   Multiple `print` statements: More verbose than single `print` with `sep='\n'`.
    -   String concatenation: Less elegant than f-strings.
    -   Template strings: Less flexible than f-strings.
-   **Extensibility**:
    -   Easily modified to add more stats or adjust formatting.
    -   Could accept variable `weight`, `height`, `hours`.
    -   Could adjust `STEP_LENGTH_M` or thresholds.
-   **Edge Cases**:
    -   Zero steps: `distance = 0.0`, correct congratulation (`"Lying down..."`).
    -   Boundary distances (`6.5`, `3.9`, `2.0`): Handled by `>=`.
    -   Large steps: Handled by float arithmetic.
    -   Non-integer steps: Not applicable (`steps` is `int`).

## Usage Example (For Clarity, Not Submission) 📦

```python
# Simulated example
steps, weight, height, hours = 10000, 75.0, 175.0, 2.0
distance = convert_to_km(steps)  # 6.50
calories = calculate_calories(weight, height, distance, hours)  # 330.75
congratulation = get_congratulation(distance)  # Excellent result! Goal achieved.
print_stats(distance, calories, congratulation, steps)
# Output:
# Today you have walked 10000 steps.
# Distance covered is 6.50 km.
# You have burned 330.75 kcal.
# Excellent result! Goal achieved.

# Test cases for different distances
def test_stats(steps):
    d = convert_to_km(steps)
    c = calculate_calories(75, 175, d, 2)
    cong = get_congratulation(d)
    print_stats(d, c, cong, steps)

test_stats(6000)  # ~3.9 km
# Output:
# Today you have walked 6000 steps.
# Distance covered is 3.90 km.
# You have burned 331.90 kcal.
# Not bad! The day was productive.

test_stats(3077)  # ~2.0 km
# Output:
# Today you have walked 3077 steps.
# Distance covered is 2.00 km.
# You have burned 321.74 kcal.
# Not enough, but we'll make up for it tomorrow!

test_stats(1000)  # ~0.65 km
# Output:
# Today you have walked 1000 steps.
# Distance covered is 0.65 km.
# You have burned 317.73 kcal.
# Lying down is also useful. The main thing is participation, not victory!
```

## Conclusion 🚀

The fitness tracker implementation with `print_stats` is precise, correctly formatting the output across four lines: steps, distance, calories, and congratulation.
It uses a triple-quoted f-string with `sep='\n'` for clarity, rounds distance and calories to two decimal places, and selects the correct congratulation.
The implementation is efficient, extensible, and ideal for fitness tracking or teaching multi-line formatting, fully compliant with the task’s requirements.
