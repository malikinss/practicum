# Lesson 1.9: Data Types 📊

## Description 📝

This lesson covers:

-   Python’s typing system: implicit, strong, and dynamic
-   Built-in data types: `None`, `bool`, numeric, sequences, sets, and dictionaries
-   Importance of data types for memory, operations, and safety

This lesson includes a detailed theoretical explanation, 1 programming practical task, and no theoretical questions, emphasizing understanding of data types.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand Python’s typing system and its implications  
✅ Identify and use built-in data types effectively  
✅ Recognize the role of types in memory and operations  
✅ Apply type casting in practical tasks like numeric summation

## Concepts & Theory 🔍

### 🔹 Python Typing

-   **Implicit**: No type declaration needed (e.g., `a = 1` is `int`).
-   **Dynamic**: Types can change at runtime (e.g., `a = 1; a = "text"`).
-   **Strong**: No automatic type coercion for incompatible operations (e.g., `1 + "2"` raises `TypeError`).

### 🔹 Built-in Data Types

-   **None**: Represents absence of value (`None`).
-   **Boolean**: `True`, `False` for logical operations.
-   **Numeric**: `int` (unlimited size), `float` (decimals), `complex` (e.g., `3+4j`).
-   **Sequences**:
    -   `list` (mutable), `tuple` (immutable), `range` (number sequences).
    -   Subclasses: `str` (text), `bytes`, `bytearray`, `memoryview` (binary).
-   **Sets**: `set` (mutable, unique), `frozenset` (immutable).
-   **Mappings**: `dict` (key-value pairs).

### 🔹 Importance of Data Types

-   **Memory**: Types determine memory allocation.
-   **Operations**: Define valid operations (e.g., `+` for numbers vs. strings).
-   **Safety**: Strong typing prevents erroneous operations.

## Practical Task 🧪

### 1️⃣ **Type Manipulation**

The lesson includes 1 practical task applying data types:

1. **`sum_numbers` Function**: Sums numbers with type casting.
    - Converts `int`, `str`, and list element to integers, returns formatted sum string.

💡 This task demonstrates type casting and string formatting in a numeric context.

## Benefits ✅

-   Understanding typing improves code flexibility and safety.
-   Knowledge of data types enables appropriate operation selection.
-   Type casting allows handling mixed data sources.
-   Practical tasks build skills for data processing.

## Recommendations 📌

-   Check types with `type()` to debug unexpected behavior.
-   Use explicit type casting (e.g., `int()`, `str()`) for compatibility.
-   Avoid mixing incompatible types to prevent `TypeError`.
-   Leverage strong typing for robust code.

## Output 📜

After completing this lesson, I now:  
✅ Understand Python’s implicit, strong, dynamic typing  
✅ Work with built-in data types like `int`, `str`, and `list`  
✅ Apply type casting in practical numeric tasks  
✅ Recognize the role of types in memory and operations

## Conclusion 🚀

Mastering Python’s data types equips me to write flexible, safe code.  
By handling mixed types in tasks like numeric summation, I’ve built a foundation for robust data processing in real-world applications. 🧑‍💻✨
