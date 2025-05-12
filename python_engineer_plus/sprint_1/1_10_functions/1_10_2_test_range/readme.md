# test_range Function Implementation

## Description 📝

The provided code implements the `test_range` function, which takes a start value, a stop value, and an arbitrary number of numbers to check.
It returns a list of numbers that fall within the specified range `[start, stop)` (inclusive of `start`, exclusive of `stop`).
For each number that is outside the range or not a valid number (integer or float), it prints the message `"Number out of range"`.
The function uses variable arguments (`*args`) to handle an undefined number of inputs and includes type checking to ensure only integers or floats are processed.
The example usage tests the function with `start=2`, `stop=8`, and numbers `1, 3, 7, 9`.

## Purpose 🎯

Intended for range-based filtering, data validation, or educational examples of variable arguments, type checking, and conditional logic in Python.

## How It Works 🔍

-   **Function Definition**:
    -   `test_range` takes:
        -   `start: Union[int, float]`: Start of the range (inclusive).
        -   `stop: Union[int, float]`: End of the range (exclusive).
        -   `*args: Union[int, float]`: Variable number of numbers to check.
    -   Returns a list of numbers (`List[Union[int, float]]`) within the range.
    -   Uses type hints for clarity.
-   **Logic**:
    -   Initializes an empty list `in_range` to store numbers within the range.
    -   Iterates over each `num` in `args`:
        -   Checks if `num` is an integer or float using `isinstance(num, (int, float))`.
        -   If not, prints `"Number out of range"` and continues.
        -   Checks if `num` is in the range `[start, stop)` using `start <= num < stop`.
        -   If in range, appends `num` to `in_range`.
        -   If out of range, prints `"Number out of range"`.
    -   Returns `in_range`.
-   **Main Code**:
    -   Calls `test_range(2, 8, 1, 3, 7, 9)` and prints the result.
-   **Behavior**:
    -   For `start=2`, `stop=8`, `args=(1, 3, 7, 9)`:
        -   `1`: `1 < 2`, prints `"Number out of range"`.
        -   `3`: `2 <= 3 < 8`, appends `3`.
        -   `7`: `2 <= 7 < 8`, appends `7`.
        -   `9`: `9 >= 8`, prints `"Number out of range"`.
    -   Returns: `[3, 7]`.
    -   Output:
        ```
        Number out of range
        Number out of range
        [3, 7]
        ```

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:
    -   Filters numbers within `[start, stop)` (inclusive start, exclusive stop).
    -   Prints `"Number out of range"` for numbers outside the range or invalid types.
    -   Returns a list of numbers in the range.
    -   Example: `test_range(2, 8, 1, 3, 7, 9)`:
        -   In range: `3, 7` (as `2 <= 3, 7 < 8`).
        -   Out of range: `1` (`1 < 2`), `9` (`9 >= 8`).
        -   Prints: `"Number out of range"` for `1` and `9`.
        -   Returns: `[3, 7]`.
-   **Correctness**:
    -   Range check: `start <= num < stop` ensures correct inclusion/exclusion.
    -   Type check: `isinstance(num, (int, float))` ensures only numbers are processed.
    -   Message printed for invalid types or out-of-range numbers.
    -   No validation needed for `start` and `stop`, as they are guaranteed valid.
-   **Output**:
    -   Prints: `"Number out of range"` for `1` and `9`.
    -   Prints: `[3, 7]`.
-   **Documentation**: Clear docstring with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `start <= num < stop` correctly implements inclusive start, exclusive stop.
    -   Type checking ensures robustness against non-numeric inputs (though not needed for the example).
    -   Empty `args` returns `[]`, which is correct.
    -   Preserves input types (int or float) in the output list.
-   **Performance**:
    -   Iteration over `args`: O(n), where n is the number of arguments.
    -   Type check: O(1) per argument.
    -   Range check and append: O(1) per argument.
    -   Total: O(n), efficient for typical input sizes.
-   **Design**:
    -   Type hints (`Union[int, float]`, `List[Union[int, float]]`) clarify input/output.
    -   Variable arguments (`*args`) handle undefined number of inputs.
    -   Single loop with clear conditions is readable.
    -   Returns list, as required.
-   **Alternatives**:
    -   List comprehension: `[num for num in args if isinstance(num, (int, float)) and start <= num < stop]` (less clear for printing messages).
    -   Filter function: `list(filter(lambda x: start <= x < stop, args))` (doesn’t handle messages or type checking).
    -   Manual validation: Redundant, as inputs are guaranteed valid.
-   **Extensibility**:
    -   Easily modified to include `stop` (change `<` to `<=`).
    -   Could add validation for `start <= stop`.
    -   Could collect out-of-range numbers instead of printing.
-   **Edge Cases**:
    -   Empty `args`: Returns `[]`.
    -   Single number: `test_range(2, 8, 5)` → `[5]`.
    -   All out of range: `test_range(2, 8, 1, 9)` → `[]`, prints messages.
    -   Boundary values: `2` (included), `8` (excluded).
    -   Non-numeric args: Prints `"Number out of range"` (handled by type check).

## Usage Example (For Clarity, Not Submission) 📦

```python
# Provided example
print(test_range(2, 8, 1, 3, 7, 9))
# Output:
# Number out of range
# Number out of range
# [3, 7]

# Additional test cases
print(test_range(1, 5, 1, 5, 3))  # [1, 3]
# Output:
# Number out of range
# [1, 3]

print(test_range(10, 20, 5, 15, 25))  # [15]
# Output:
# Number out of range
# Number out of range
# [15]

print(test_range(2, 8, 2.5, 7.9, 8.0))  # [2.5, 7.9]
# Output:
# Number out of range
# [2.5, 7.9]

print(test_range(1, 10))  # []
# Output: []
```

## Conclusion 🚀

The `test_range` function implementation is precise, correctly filtering numbers within the range `[2, 8)` for the input `1, 3, 7, 9`, returning `[3, 7]`, and printing `"Number out of range"` for `1` and `9`.
It handles variable arguments, type checking, and range conditions efficiently.
The implementation is clear, robust, and fully compliant with the task’s requirements, making it ideal for range-based filtering or teaching variable arguments and conditional logic.
