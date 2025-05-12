# Lesson 1.2: Numeric Types and None 🔢

## Description 📝

This lesson covers:

-   The importance of practice in learning programming
-   Numeric types in Python: `int`, `float`, `complex`, and `Decimal`
-   Arithmetic operations and operator precedence
-   The `None` type for representing absence of value

This lesson includes a detailed theoretical explanation, 3 programming practical tasks, and no theoretical questions, emphasizing hands-on practice.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand Python’s numeric types and their applications  
✅ Perform arithmetic operations with proper precedence and precision  
✅ Use the `None` type appropriately  
✅ Apply numeric calculations to practical scenarios like fitness tracking

## Concepts & Theory 🔍

### 🔹 Importance of Practice

-   **Purpose**: Reinforces learning through hands-on coding.
-   **Dale’s Cone**: 90% retention from practice vs. 10% from reading.
-   **Application**: Write and test code, culminating in a fitness tracker project.

### 🔹 Numeric Types

-   **Integers (`int`)**: Whole numbers, e.g., `432_246_123` (underscore for readability).
-   **Floats (`float`)**: Decimal numbers, e.g., `2.345`; prone to precision issues.
-   **Complex Numbers (`complex`)**: Real + imaginary parts, not covered in depth.
-   **Decimal Module**: High-precision arithmetic, e.g., `Decimal('3.3') + Decimal('4.1') = 7.4`.

### 🔹 Arithmetic Operations

-   **Operators**: `+`, `-`, `*`, `/`, `**`, `//`, `%`, and combined assignments (`+=`, etc.).
-   **Features**: `/` yields `float`, `//` for integer division, `%` for remainder.
-   **Precedence**: `**` > `*`, `/`, `//`, `%` > `+`, `-`; parentheses override.

### 🔹 `None` Type

-   **Purpose**: Represents absence of value or default state.
-   **Usage**: `a = None` can later be reassigned to other types.

## Practical Task 🧪

### 1️⃣ **Numeric Calculations**

The lesson includes 3 practical tasks, each applying numeric types and operations:

1. **`calculate_week_dist` Function**: Weekly distance summation.

    - Uses `Decimal` for precise float summation, rounds to 3 decimal places.

2. **`convert_seconds` Function**: Time conversion.

    - Converts seconds to a tuple of days, hours, minutes, seconds.

3. **`calculate_calories` Function**: Calorie expenditure.
    - Applies a formula with `Decimal` for precision, rounds to 2 decimal places.

💡 These tasks demonstrate numeric precision and arithmetic in fitness and time applications.

## Benefits ✅

-   `Decimal` ensures accurate calculations for critical applications.
-   Understanding operator precedence prevents logical errors.
-   Practice reinforces coding skills per Dale’s Cone.
-   `None` provides a clear way to represent undefined states.

## Recommendations 📌

-   Follow PEP8 for readable code (spaces around operators).
-   Use `Decimal` for precision in financial or fitness calculations.
-   Practice regularly to master numeric operations.
-   Use parentheses to clarify operator precedence.

## Output 📜

After completing this lesson, I now:  
✅ Work with `int`, `float`, and `Decimal` for numeric tasks  
✅ Apply arithmetic operations with correct precedence  
✅ Use `None` to represent absent values  
✅ Implement precise calculations for fitness tracking scenarios

## Conclusion 🚀

Mastering numeric types and `None` equips me to handle precise calculations in Python.  
From calorie tracking to time conversions, these skills lay a strong foundation for practical programming, reinforced by hands-on practice. 🧑‍💻✨
