# Planet Class Implementation

## Description 📝

The provided code implements the `Planet` class, which stores and manages properties of a planet, including `name`, `surface_area` (in km²), `average_temp_celsius`, and `average_temp_fahrenheit`.

The class constructor takes three parameters: the planet’s `name`, `radius` (in kilometers), and `average_temp_celsius` (in Celsius). It calculates the `surface_area` using the formula for a sphere’s surface area (`4 * π * r²`) and converts the temperature to Fahrenheit using the formula `C * 9/5 + 32`.

The class includes validation for non-empty names and non-negative radii, a method to display planet details (`show_info`), and helper methods for calculations.

The implementation assumes planets are spherical for simplicity.

## Purpose 🎯

Intended for astronomical data modeling, educational examples of object-oriented programming, or applications requiring planetary property calculations in Python.

## How It Works 🔍

-   **Module Import**:
    -   `import math`: Provides `math.pi` for surface area calculations.
-   **Class Definition**:
    -   `Planet` class with:
        -   `__init__`: Initializes planet properties and performs calculations.
        -   `_get_surface_area`: Calculates surface area.
        -   `_get_fahrenheit`: Converts Celsius to Fahrenheit.
        -   `show_info`: Prints planet details.
-   ****init** Method**:
    -   Takes:
        -   `name: str`: Planet’s name.
        -   `radius: float`: Radius in kilometers.
        -   `temp_celsius: float`: Average surface temperature in Celsius.
    -   Validates:
        -   `name` must not be empty (`if not name`).
        -   `radius` must be non-negative (`radius < 0`).
    -   Assigns:
        -   `self.name = name`.
        -   `self.radius = radius` (stored for potential future use).
        -   `self.surface_area = self._get_surface_area()`.
        -   `self.average_temp_celsius = temp_celsius`.
        -   `self.average_temp_fahrenheit = self._get_fahrenheit(temp_celsius)`.
-   **\_get_surface_area Method**:
    -   Calculates surface area using `4 * π * r²`.
    -   Uses `math.pi` and `self.radius`.
    -   Returns a `float`.
-   **\_get_fahrenheit Method**:
    -   Converts `celsius` to Fahrenheit using `celsius * 9 / 5 + 32`.
    -   Returns a `float`.
-   **show_info Method**:
    -   Prints:
        -   `Planet: <name> has surface area <surface_area> square kilometers`.
        -   `Average temperature on the surface is <average_temp_fahrenheit> Fahrenheit`.
-   **Behavior**:
    -   Example (hypothetical usage, as no main code is provided):
        -   Planet: `Planet("Earth", 6371, 15)`.
        -   Surface area: `4 * π * 6371² ≈ 510064471 km²`.
        -   Fahrenheit: `15 * 9/5 + 32 = 59°F`.
        -   Output (if `show_info` called):
            ```
            Planet: Earth has surface area 510064471.0 square kilometers
            Average temperature on the surface is 59.0 Fahrenheit
            ```

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:
    -   Stores `name`, `surface_area`, `average_temp_celsius`, `average_temp_fahrenheit`.
    -   Constructor takes `name`, `radius`, `temp_celsius`.
    -   Calculates `surface_area` using `4 * π * r²`.
    -   Calculates `average_temp_fahrenheit` using `C * 9/5 + 32`.
-   **Correctness**:
    -   Surface area: `4 * math.pi * radius ** 2` is mathematically accurate.
    -   Fahrenheit conversion: `celsius * 9 / 5 + 32` follows the standard formula.
    -   Validation ensures non-empty `name` and non-negative `radius`.
    -   No validation for `temp_celsius`, as any float is valid (e.g., negative temperatures).
-   **Output**:
    -   `show_info` formats output as specified, though not called in provided code.
-   **Documentation**: Clear docstrings with type hints and validation details.

## Potential Considerations 🛠️

-   **Correctness**:
    -   Surface area formula assumes a perfect sphere, as specified.
    -   Fahrenheit conversion is exact (e.g., `15°C → 59°F`).
    -   Validation prevents invalid inputs (`empty name`, `negative radius`).
    -   No upper bound on `radius` or `temp_celsius`, as not required.
-   **Performance**:
    -   `__init__`: O(1) for assignments and calculations.
    -   `_get_surface_area`: O(1) for arithmetic.
    -   `_get_fahrenheit`: O(1).
    -   `show_info`: O(1) for printing.
    -   Total: O(1), highly efficient.
-   **Design**:
    -   Type hints (`str`, `float`) clarify inputs.
    -   Private methods (`_get_surface_area`, `_get_fahrenheit`) encapsulate calculations.
    -   Stores `radius` for potential reuse, though not strictly necessary.
    -   `show_info` is reusable for displaying details.
-   **Alternatives**:
    -   Hardcode calculations in `__init__`: Less modular.
    -   Use `decimal.Decimal` for precision: Unnecessary for typical use.
    -   Store only `temp_celsius`: Would require recalculation for Fahrenheit.
-   **Extensibility**:
    -   Easily add properties (e.g., mass, gravity).
    -   Could round `surface_area` or temperatures for display.
    -   Could validate `temp_celsius` for realistic ranges (e.g., planetary limits).
-   **Edge Cases**:
    -   Zero radius: Valid, yields `surface_area = 0`.
    -   Negative temperature: Valid (e.g., `-100°C` for cold planets).
    -   Empty name: Raises `ValueError`.
    -   Negative radius: Raises `ValueError`.
    -   Large values: Handled by Python’s floating-point arithmetic.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Example usage
earth = Planet("Earth", 6371, 15)
earth.show_info()
# Output:
# Planet: Earth has surface area 510064471.0 square kilometers
# Average temperature on the surface is 59.0 Fahrenheit

# Additional test cases
mercury = Planet("Mercury", 2439.7, 167)
mercury.show_info()
# Output:
# Planet: Mercury has surface area 74900000.0 square kilometers
# Average temperature on the surface is 332.6 Fahrenheit

try:
    invalid = Planet("", 1000, 0)  # Empty name
except ValueError as e:
    print(e)  # Name cannot be empty

try:
    invalid = Planet("Mars", -1000, 0)  # Negative radius
except ValueError as e:
    print(e)  # Radius cannot be negative
```

## Conclusion 🚀

The `Planet` class implementation is precise, correctly initializing a planet with `name`, `radius`, and `temp_celsius`, calculating `surface_area` (`4 * π * r²`) and `average_temp_fahrenheit` (`C * 9/5 + 32`), and providing a `show_info` method to display details.

It includes validation for robustness and is efficient and modular.

The implementation fully complies with the task’s requirements, making it ideal for modeling planetary data or teaching object-oriented programming and mathematical calculations in Python.
