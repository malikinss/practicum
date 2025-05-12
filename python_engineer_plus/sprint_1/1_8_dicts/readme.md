# Lesson 1.8: Dictionaries 📖

## Description 📝

This lesson covers:

-   Dictionaries: mutable, unordered collections of key-value pairs
-   Creating, accessing, and modifying dictionaries
-   Dictionary methods and iteration techniques

This lesson includes a detailed theoretical explanation, 1 programming practical task, and no theoretical questions, emphasizing practical dictionary manipulation.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand dictionaries and their key-value structure  
✅ Create and manipulate dictionaries using methods and comprehensions  
✅ Iterate over dictionaries for data processing  
✅ Apply dictionaries to practical tasks like movie recommendations

## Concepts & Theory 🔍

### 🔹 Dictionaries

-   **Purpose**: Store key-value pairs; keys are unique and immutable, values can be any type.
-   **Features**: Mutable, unordered, efficient key-based access.
-   **Use Case**: Structured data storage (e.g., movie ratings).

### 🔹 Creation

-   **Literal**: `{'key': value}`.
-   **Function**: `dict([(key, value)])` or `dict.fromkeys(keys, default)`.
-   **Zip**: `dict(zip(keys, values))`.
-   **Comprehension**: `{key: value for var in iterable}`.

### 🔹 Operations

-   **Access**: `dict[key]` or `dict.get(key, default)`.
-   **Modify**: `dict[key] = value`, `update(dict2)`.
-   **Delete**: `del dict[key]`, `pop(key, default)`, `clear()`.
-   **Views**: `keys()`, `values()`, `items()` for iteration.
-   **Copy**: `copy()` for independent copies.

### 🔹 Iteration

-   **Keys**: `for key in dict`.
-   **Values**: `for value in dict.values()`.
-   **Pairs**: `for key, value in dict.items()`.

## Practical Task 🧪

### 1️⃣ **Dictionary Manipulation**

The lesson includes 1 practical task applying dictionaries:

1. **`process_movies` Function**: Processes movie ratings and reviews.
    - Filters movies by rating, updates `favorites` dictionary, prints messages.

💡 This task demonstrates dictionary operations in a movie recommendation context.

## Benefits ✅

-   Dictionaries provide efficient key-based data access.
-   Flexible creation methods support diverse use cases.
-   Iteration methods simplify data processing.
-   Practical tasks build skills for structured data management.

## Recommendations 📌

-   Use `get()` to avoid `KeyError` for missing keys.
-   Prefer `items()` for key-value iteration.
-   Use `copy()` to avoid unintended modifications.
-   Ensure keys are immutable to prevent errors.

## Output 📜

After completing this lesson, I now:  
✅ Create and manipulate dictionaries with various methods  
✅ Iterate over dictionaries for data extraction  
✅ Apply dictionaries to practical tasks like movie processing  
✅ Implement efficient solutions for structured data

## Conclusion 🚀

Mastering dictionaries equips me to manage structured data effectively in Python.  
By processing movie ratings and reviews, I’ve honed skills for real-world applications like recommendation systems and data organization. 🧑‍💻✨
