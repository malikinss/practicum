# find_quadrant and get_coordinates Implementation

## Description 📝

The provided code implements two functions: `find_quadrant` and `get_coordinates`.
The `find_quadrant` function determines the quadrant (or axis) of a point on a coordinate plane given its `x` and `y` coordinates.
The `get_coordinates` function prompts the user to input `x` and `y` coordinates and returns them as a tuple.
The program uses these functions to read coordinates, determine the quadrant, and print the result.
It handles all cases, including points on axes, and uses clear conditional logic for quadrant identification.

## Purpose 🎯

Intended for applications requiring coordinate plane analysis, such as geometry tools, educational exercises, or interactive programs teaching coordinate systems.

## How It Works 🔍

-   **find_quadrant Function**:
    -   Takes two parameters: `x` and `y` (floats representing coordinates).
    -   Returns a string indicating the quadrant or "Point on axis" if the point lies on an axis.
    -   Logic:
        -   If `x == 0` or `y == 0`, returns "Point on axis" (includes origin, x-axis, or y-axis).
        -   If `x > 0` and `y > 0`, returns "First Quadrant".
        -   If `x < 0` and `y > 0`, returns "Second Quadrant".
        -   If `x < 0` and `y < 0`, returns "Third Quadrant".
        -   Otherwise (`x > 0` and `y < 0`), returns "Fourth Quadrant".
    -   Uses type hints (`float`, `str`) for clarity.
-   **get_coordinates Function**:
    -   Prompts the user to input `x` and `y` coordinates using `input()`.
    -   Converts inputs to floats using `float()`.
    -   Returns a tuple `(x, y)`.
    -   Uses type hints (`Tuple[float, float]`) for clarity.
-   **Main Code**:
    -   Calls `get_coordinates()` to get `x` and `y`.
    -   Passes `x`, `y` to `find_quadrant` and prints the result.
-   **Behavior**:
    -   Reads user input for coordinates.
    -   Determines the quadrant or axis location.
    -   Outputs a clear string (e.g., "First Quadrant", "Point on axis").
    -   Handles all possible coordinate values, including zero and negative numbers.

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:
    -   Determines the quadrant of a point based on `x` and `y` coordinates.
    -   Handles axis cases (x-axis, y-axis, origin).
    -   Example cases:
        -   `(1, 1)` → "First Quadrant" (`x > 0`, `y > 0`).
        -   `(-1, 1)` → "Second Quadrant" (`x < 0`, `y > 0`).
        -   `(-1, -1)` → "Third Quadrant" (`x < 0`, `y < 0`).
        -   `(1, -1)` → "Fourth Quadrant" (`x > 0`, `y < 0`).
        -   `(0, 1)`, `(1, 0)`, `(0, 0)` → "Point on axis".
-   **Input Handling**:
    -   `get_coordinates` reads `x` and `y` from user input.
    -   Converts inputs to floats, supporting decimals and negative values.
    -   Example: User enters `3.5` and `-2.7` → `(3.5, -2.7)`.
-   **Output**:
    -   Prints a string describing the quadrant or axis.
    -   Matches required format (e.g., "First Quadrant", "Point on axis").
-   **Correctness**:
    -   Conditional logic covers all quadrants and axis cases.
    -   Checks `x == 0 or y == 0` first to prioritize axis detection.
    -   Quadrant checks use simple comparisons (`> 0`, `< 0`).
    -   No validation needed, as inputs are guaranteed convertible to floats.
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   Axis check (`x == 0 or y == 0`) correctly identifies points on the x-axis, y-axis, or origin.
    -   Quadrant conditions are mutually exclusive and cover all non-axis cases.
    -   Float inputs handle decimals and negative values accurately.
    -   No ambiguity in quadrant assignment (e.g., `x > 0` and `y < 0` is only Fourth Quadrant).
-   **Performance**:
    -   `find_quadrant`: O(1) for fixed comparisons.
    -   `get_coordinates`: O(1) for reading and converting two inputs.
    -   Total: O(1), highly efficient for any input.
-   **Design**:
    -   Type hints (`float`, `str`, `Tuple[float, float]`) clarify signatures.
    -   Separate functions for input (`get_coordinates`) and logic (`find_quadrant`) improve modularity.
    -   Clear string outputs are user-friendly.
-   **Alternatives**:
    -   Hardcoded quadrant mapping: Less readable than conditionals.
    -   Return quadrant number (1, 2, 3, 4): Doesn’t match string output requirement.
    -   No axis check: Would incorrectly assign axis points to quadrants.
-   **Extensibility**:
    -   Easily modified to return quadrant numbers or handle 3D coordinates.
    -   Could add input validation (e.g., ensure valid float conversion) if needed.
-   **Edge Cases**:
    -   Zero coordinates: `(0, 0)`, `(0, 1)`, `(1, 0)` → "Point on axis".
    -   Negative coordinates: Handled correctly (e.g., `(-1, -1)` → "Third Quadrant").
    -   Decimal coordinates: Supported via float conversion.
    -   Large values: No overflow issues with floats.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Example usage with manual inputs (simulating user input)
def test_find_quadrant(x, y):
    print(f"Point ({x}, {y}): {find_quadrant(x, y)}")

test_find_quadrant(1, 1)      # Point (1, 1): First Quadrant
test_find_quadrant(-1, 1)     # Point (-1, 1): Second Quadrant
test_find_quadrant(-1, -1)    # Point (-1, -1): Third Quadrant
test_find_quadrant(1, -1)     # Point (1, -1): Fourth Quadrant
test_find_quadrant(0, 1)      # Point (0, 1): Point on axis
test_find_quadrant(1, 0)      # Point (1, 0): Point on axis
test_find_quadrant(0, 0)      # Point (0, 0): Point on axis
test_find_quadrant(3.5, -2.7) # Point (3.5, -2.7): Fourth Quadrant

# Interactive example (requires user input)
x, y = get_coordinates()  # E.g., user enters 2 and -3
print(find_quadrant(x, y))  # Fourth Quadrant
```

## Conclusion 🚀

The `find_quadrant` and `get_coordinates` implementation is precise, correctly determining the quadrant or axis of a point based on user-provided `x` and `y` coordinates.
It handles all cases (quadrants, axes, origin) with clear conditional logic, supports float inputs, and outputs user-friendly strings.
The implementation is efficient, extensible, and ideal for coordinate-based applications or teaching coordinate systems, fully compliant with the task’s requirements.
