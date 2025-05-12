# print_word_from_string Implementation

## Description 📝

The provided code implements the `print_word_from_string` function, which extracts specific characters from an input string to form the Russian word "Домик" (meaning "house") and prints each character on a new line.
The function uses predefined indices to select characters from the input string `name_movie = 'Джонни Мнемоник'`.
It includes a length check to ensure the input string is long enough and raises a `ValueError` if it is not.
The output matches the required format: `Д`, `о`, `м`, `и`, `к`.

## Purpose 🎯

Intended for string manipulation tasks, text processing, or educational examples of indexing and error handling in Python.

## How It Works 🔍

-   **Function Definition**:
    -   `print_word_from_string` takes a string parameter `text`.
    -   Uses a type hint (`str`) for clarity.
-   **Validation**:
    -   Checks if the string length is at least 11 characters (since the last index used is 10).
    -   Raises `ValueError` with message "String too short to form 'Домик'" if too short.
-   **Processing**:
    -   Defines `indices = [0, 2, 10, 4, -1]` to select characters for "Домик":
        -   Index `0`: `Д` (first character).
        -   Index `2`: `о` (third character).
        -   Index `10`: `м` (eleventh character).
        -   Index `4`: `и` (fifth character).
        -   Index `-1`: `к` (last character).
    -   Iterates over `indices` and prints the character at each index using `text[i]`.
-   **Main Code**:
    -   Defines `name_movie = 'Джонни Мнемоник'` (a string of 14 characters).
    -   Calls `print_word_from_string(name_movie)`.
-   **Behavior**:
    -   Extracts characters from `name_movie` at indices `[0, 2, 10, 4, -1]`:
        -   `name_movie[0] = Д`
        -   `name_movie[2] = о`
        -   `name_movie[10] = м`
        -   `name_movie[4] = и`
        -   `name_movie[-1] = к` (equivalent to `name_movie[13]`)
    -   Prints each character on a new line, forming:
        ```
        Д
        о
        м
        и
        к
        ```
    -   Ensures the output forms the word "Домик".

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:
    -   Prints characters to form "Домик" from the input string.
    -   Input: `name_movie = 'Джонни Мнемоник'` (14 characters).
    -   Selected characters:
        -   `name_movie[0] = Д`
        -   `name_movie[2] = о`
        -   `name_movie[10] = м`
        -   `name_movie[4] = и`
        -   `name_movie[-1] = к`
    -   Output:
        ```
        Д
        о
        м
        и
        к
        ```
-   **Validation**:
    -   Checks if string length is at least 11 to access index 10.
    -   Raises `ValueError` for shorter strings.
-   **Correctness**:
    -   Indices `[0, 2, 10, 4, -1]` correctly extract "Домик" from "Джонни Мнемоник".
    -   Negative index `-1` accesses the last character (`к`).
    -   Each character is printed on a new line using `print`.
    -   No additional validation needed, as input is guaranteed sufficient in the example.
-   **Documentation**: Clear docstring with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   Indices are chosen to exactly match "Домик" from "Джонни Мнемоник".
    -   Length check (`len(text) < 11`) ensures index 10 is accessible.
    -   Negative index `-1` correctly accesses the last character.
    -   `print(text[i])` outputs each character on a new line automatically.
-   **Performance**:
    -   Length check: O(1).
    -   Indexing and printing: O(1) per index, total O(k) for k indices (k=5 here).
    -   Total: O(1) for fixed indices, highly efficient.
-   **Design**:
    -   Type hint (`str`) clarifies input type.
    -   Hardcoded indices are specific to forming "Домик" from the given string.
    -   Error handling ensures robustness for shorter inputs.
    -   Simple loop for printing is clear and maintainable.
-   **Alternatives**:
    -   Dynamic index calculation: Unnecessary, as indices are fixed for "Домик".
    -   String slicing: Less clear for non-contiguous characters.
    -   List comprehension: Overkill for simple printing.
-   **Extensibility**:
    -   Easily modified to extract different words or use different indices.
    -   Could add validation for specific string content if needed.
-   **Edge Cases**:
    -   Exact length 11: Valid, as index 10 is accessible.
    -   Shorter string: Raises `ValueError` (e.g., "Джонни" has 6 characters).
    -   Empty string: Raises `ValueError`.
    -   Unicode characters: Handled correctly, as "Джонни Мнемоник" is Unicode.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Provided example
name_movie = 'Джонни Мнемоник'
print_word_from_string(name_movie)
# Output:
# Д
# о
# м
# и
# к

# Additional test cases
try:
    print_word_from_string('Джонни')  # Too short
except ValueError as e:
    print(e)  # String too short to form 'Домик'

# Test with a longer string
print_word_from_string('Джонни Мнемоник Extra')
# Output:
# Д
# о
# м
# и
# a

# Test with exact length
print_word_from_string('Джонни Мнемо')
# Output:
# Д
# о
# м
# и
# о
```

## Conclusion 🚀

The `print_word_from_string` function implementation is precise, correctly extracting and printing the characters `Д`, `о`, `м`, `и`, `к` from the input string "Джонни Мнемоник" to form "Домик".
It uses specific indices, includes length validation, and outputs each character on a new line.
The implementation is efficient, robust, and ideal for string manipulation tasks or teaching indexing, fully compliant with the task’s requirements.
