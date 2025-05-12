# swap_first_last Function Implementation

## Description 📝

The provided code implements the `swap_first_last` function, which normalizes Master Yoda's sentences by swapping the first and last words in a list of words representing a sentence.
The swap is performed in-place, modifying the input list directly without creating a new object.
The function checks if the list has at least two words to ensure a valid swap.
The code then applies this function to the example list `force_words = ['you', 'the force', 'be', 'with', 'May']` and prints the modified list.

## Purpose 🎯

Intended for text processing, list manipulation, or educational examples of in-place operations, indexing, and tuple unpacking in Python.

## How It Works 🔍

-   **Function Definition**:
    -   `swap_first_last` takes a list of strings (`sentence: List[str]`).
    -   Returns `None`, modifying the input list in-place.
    -   Uses a type hint for clarity.
-   **Logic**:
    -   Checks if the list has at least 2 elements (`len(sentence) >= 2`) to ensure a valid swap.
    -   If true, swaps the first (`sentence[0]`) and last (`sentence[-1]`) elements using tuple unpacking:
        -   `sentence[0], sentence[-1] = sentence[-1], sentence[0]`.
    -   If the list has fewer than 2 elements, does nothing (no swap needed).
-   **Main Code**:
    -   Defines `force_words = ['you', 'the force', 'be', 'with', 'May']`.
    -   Calls `swap_first_last(force_words)`.
    -   Prints the modified `force_words`.
-   **Behavior**:
    -   For `force_words`:
        -   Original: `['you', 'the force', 'be', 'with', 'May']`.
        -   Swaps `sentence[0] = 'you'` and `sentence[-1] = 'May'`.
        -   Modified: `['May', 'the force', 'be', 'with', 'you']`.
    -   Modifies the list in-place, as required.
    -   Outputs: `['May', 'the force', 'be', 'with', 'you']`.

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:
    -   Swaps the first and last words of the input list.
    -   Example: `['you', 'the force', 'be', 'with', 'May']` → `['May', 'the force', 'be', 'with', 'you']`.
    -   Performs the swap in-place (modifies `sentence` directly).
-   **In-Place Modification**:
    -   Uses tuple unpacking (`sentence[0], sentence[-1] = sentence[-1], sentence[0]`) to swap without creating a new list.
    -   No temporary lists or copies are created.
-   **Correctness**:
    -   Checks `len(sentence) >= 2` to avoid errors on empty or single-word lists.
    -   Uses `sentence[-1]` for the last element, equivalent to `sentence[len(sentence)-1]`.
    -   Preserves all other elements (e.g., `'the force', 'be', 'with'` remain unchanged).
    -   No validation needed beyond length, as input is guaranteed to be a list of strings.
-   **Output**:
    -   Prints the modified list: `['May', 'the force', 'be', 'with', 'you']`.
-   **Documentation**: Clear docstring with type hint.

## Potential Considerations 🛠️

-   **Correctness**:
    -   Tuple unpacking ensures atomic swap, avoiding temporary variables.
    -   Length check prevents index errors for lists with 0 or 1 element.
    -   `sentence[-1]` correctly accesses the last element.
    -   Swap works for lists of any length ≥ 2.
-   **Performance**:
    -   Length check: O(1).
    -   Swap operation: O(1) for indexing and assignment.
    -   Total: O(1), highly efficient.
-   **Design**:
    -   Type hint (`List[str]`) clarifies input type.
    -   In-place modification meets the requirement to avoid new objects.
    -   Simple conditional ensures robustness.
    -   Returns `None`, as the task requires modification, not returning a value.
-   **Alternatives**:
    -   Temporary variable: `temp = sentence[0]; sentence[0] = sentence[-1]; sentence[-1] = temp` (more verbose).
    -   List slicing: Creates a new list, violating in-place requirement.
    -   `collections.deque.rotate`: Overkill and not specific to first/last swap.
-   **Extensibility**:
    -   Easily modified to swap other positions (e.g., second and second-to-last).
    -   Could add validation for non-empty strings if needed.
-   **Edge Cases**:
    -   Empty list: `len(sentence) = 0`, no swap (valid, does nothing).
    -   Single element: `len(sentence) = 1`, no swap (valid, does nothing).
    -   Two elements: Swaps correctly (e.g., `['a', 'b']` → `['b', 'a']`).
    -   Long lists: Works correctly, only affects first and last.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Provided example
force_words = ['you', 'the force', 'be', 'with', 'May']
swap_first_last(force_words)
print(force_words)  # ['May', 'the force', 'be', 'with', 'you']

# Additional test cases
test = ['a', 'b']
swap_first_last(test)
print(test)  # ['b', 'a']

test = ['only']
swap_first_last(test)
print(test)  # ['only'] (no swap, len < 2)

test = []
swap_first_last(test)
print(test)  # [] (no swap, len < 2)

test = ['1', '2', '3', '4', '5']
swap_first_last(test)
print(test)  # ['5', '2', '3', '4', '1']
```

## Conclusion 🚀

The `swap_first_last` function implementation is precise, correctly swapping the first and last words of a sentence in-place without creating a new object.
It handles the example `force_words` list, producing `['May', 'the force', 'be', 'with', 'you']`, and includes a length check for robustness.
The implementation is efficient, simple, and fully compliant with the task’s requirements, making it ideal for text processing or teaching in-place list operations.
