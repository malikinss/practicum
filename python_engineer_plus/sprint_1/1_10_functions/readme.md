# Lesson 1.10: Functions 🛠️

## Description 📝

This lesson covers:

-   Functions: reusable code blocks for processing data
-   Parameters, arguments, and return values
-   Advanced features: default parameters, `*args`, `**kwargs`, and unpacking
-   Best practices for function design and usage

This lesson includes a detailed theoretical explanation, 2 programming practical tasks, and no theoretical questions, emphasizing practical function implementation.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Define and use functions to modularize code  
✅ Handle variable arguments and default parameters  
✅ Apply functions to tasks like statistical calculations and range filtering  
✅ Follow best practices for readable, reusable functions

## Concepts & Theory 🔍

### 🔹 Functions

-   **Purpose**: Encapsulate reusable logic; process inputs and return outputs.
-   **Structure**: Defined with `def`, include parameters, body, and optional `return`.
-   **Types**: Built-in (`print()`, `str()`) and user-defined.

### 🔹 Parameters and Arguments

-   **Parameters**: Variables in function definition.
-   **Arguments**: Values passed during function call.
-   **Types**: Positional (by order), named (by parameter name), default (optional).

### 🔹 Advanced Features

-   **`*args`**: Accepts variable positional arguments as a tuple.
-   **`**kwargs`\*\*: Accepts variable named arguments as a dictionary.
-   **Unpacking**: `*` for iterables (e.g., `*list`), `**` for dictionaries.
-   **Empty Functions**: Use `pass` or `...` as placeholders.

### 🔹 Best Practices

-   Use `snake_case` for function names (PEP8).
-   Return values instead of printing for flexibility.
-   Avoid deep condition nesting; use early `return`.
-   Leverage default parameters and variable arguments for versatility.

## Practical Task 🧪

### 1️⃣ **Function Implementation**

The lesson includes 2 practical tasks applying functions:

1. **`get_mean` Function**: Calculates arithmetic mean.

    - Computes mean of a number list, returns `0.0` for empty lists, rounds to 2 decimals.

2. **`test_range` Function**: Filters numbers in a range.
    - Checks if numbers are within `[start, stop)`, prints errors for invalid inputs, uses `*args`.

💡 These tasks demonstrate function design for statistical and filtering applications.

## Benefits ✅

-   Functions promote code reuse and modularity.
-   Variable arguments enable flexible function signatures.
-   Early returns simplify logic and improve readability.
-   Practical tasks build skills for data processing and validation.

## Recommendations 📌

-   Use descriptive function names for clarity.
-   Validate inputs to handle edge cases (e.g., empty lists).
-   Prefer `*args`/`**kwargs` for variable inputs.
-   Follow PEP8 for consistent formatting (no spaces around `=` in defaults).

## Output 📜

After completing this lesson, I now:  
✅ Define functions with parameters and return values  
✅ Use `*args` and default parameters for flexibility  
✅ Apply functions to tasks like mean calculation and range filtering  
✅ Write modular, readable code following best practices

## Conclusion 🚀

Mastering functions empowers me to create modular, reusable Python code.  
From calculating means to filtering ranges, I’ve developed skills to tackle diverse programming challenges efficiently. 🧑‍💻✨
