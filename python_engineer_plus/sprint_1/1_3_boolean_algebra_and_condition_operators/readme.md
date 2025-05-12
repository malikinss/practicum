# Lesson 1.3: Conditional Operators and the Bool Type 🔍

## Description 📝

This lesson covers:

-   Conditional operators (`if`, `else`, `elif`) for branching
-   The ternary operator for concise conditionals
-   The `bool` type and logical operators (`and`, `or`, `not`)
-   Comparison operators and nested conditions

This lesson includes a detailed theoretical explanation, 1 programming practical task, and no theoretical questions, emphasizing practical application of conditional logic.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand and implement branching with conditional operators  
✅ Use the `bool` type and logical operators for decision-making  
✅ Apply comparison operators and ternary expressions effectively  
✅ Solve practical problems like coordinate quadrant identification

## Concepts & Theory 🔍

### 🔹 Branching with Conditional Operators

-   **Purpose**: Alter program flow based on conditions.
-   **Operators**:
    -   `if`: Executes code if condition is `True`.
    -   `else`: Handles `False` case.
    -   `elif`: Checks additional conditions sequentially.

### 🔹 Ternary Operator

-   **Purpose**: Compact `if...else` for value assignment.
-   **Syntax**: `value_if_true if condition else value_if_false`.

### 🔹 Nested Conditions

-   **Purpose**: Handle complex logic with `if` inside `if`.
-   **Drawbacks**: Can reduce readability; prefer `elif` for flatter code.

### 🔹 Comparison Operators

-   **Operators**: `<`, `>`, `<=`, `>=`, `==`, `!=`.
-   **Result**: Return `bool` (`True` or `False`).

### 🔹 Logical Type `bool`

-   **Values**: `True`, `False` (subclass of `int`: `True=1`, `False=0`).
-   **Truthiness**: Non-zero numbers, non-empty objects are `True`; `0`, `None`, empty objects are `False`.
-   **None Check**: Use `is` (e.g., `x is None`), not `==`.

### 🔹 Logical Operators

-   **AND (`and`)**: `True` if both operands are `True`.
-   **OR (`or`)**: `True` if at least one operand is `True`.
-   **NOT (`not`)**: Inverts truth value.

## Practical Task 🧪

### 1️⃣ **Conditional Logic Application**

The lesson includes 1 practical task applying conditional operators:

1. **`find_quadrant` and `get_coordinates` Functions**: Coordinate quadrant identification.
    - `find_quadrant`: Determines quadrant or axis for given `x`, `y`.
    - `get_coordinates`: Reads user input as a tuple of coordinates.

💡 This task demonstrates conditional logic for geometric analysis.

## Benefits ✅

-   Conditional operators enable flexible program control.
-   Logical operators simplify complex condition checks.
-   Ternary operator reduces code for simple decisions.
-   `bool` type ensures clear truth value handling.

## Recommendations 📌

-   Use `elif` over nested `if` for readability.
-   Check `None` with `is` to avoid errors.
-   Follow PEP8 for consistent code formatting.
-   Test conditions thoroughly to ensure correct logic.

## Output 📜

After completing this lesson, I now:  
✅ Implement branching with `if`, `else`, and `elif`  
✅ Use logical and comparison operators for decision-making  
✅ Apply conditional logic to practical problems like quadrant detection

## Conclusion 🚀

Mastering conditional operators and the `bool` type empowers me to control program flow effectively.  
By applying these concepts to tasks like coordinate analysis, I build a strong foundation for dynamic Python programming. 🧑‍💻✨
