# Lesson 1.6: Sequences (Part 2) 📋

## Description 📝

This lesson covers:

-   Lists: mutable, ordered sequences with methods and comprehensions
-   Tuples: immutable, ordered sequences for data protection
-   Operations like sorting, indexing, and unpacking for both

This lesson includes a detailed theoretical explanation, 3 programming practical tasks, and no theoretical questions, emphasizing practical sequence manipulation.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Create and manipulate lists using methods and comprehensions  
✅ Use tuples for immutable, efficient data storage  
✅ Apply sequence operations like swapping and pairing  
✅ Solve practical problems like fitness data aggregation

## Concepts & Theory 🔍

### 🔹 Lists

-   **Purpose**: Mutable, ordered collections of arbitrary types.
-   **Creation**: `list()`, literals `[]`, or list comprehensions `[expr for x in iterable]`.
-   **Methods**: `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `index()`, `count()`, `sort()`, `reverse()`, `copy()`, `clear()`.
-   **Unpacking**: Assign list elements to variables (e.g., `a, b = [1, 2]`).

### 🔹 Tuples

-   **Purpose**: Immutable, ordered sequences for data safety.
-   **Creation**: `tuple()`, literals `()`, or comma-separated values (e.g., `1, 2`).
-   **Operations**: Indexing, unpacking, `sorted()` (returns list); no in-place changes.
-   **Benefits**: Less memory, faster access, hashable for dictionary keys.

## Practical Task 🧪

### 1️⃣ **Sequence Manipulation**

The lesson includes 3 practical tasks applying lists and tuples:

1. **`generate_squares` Function**: Creates perfect squares list.

    - Uses list comprehension for `[1, 4, 9, ..., 100]`.

2. **`swap_first_last` Function**: Swaps first/last list elements.

    - Modifies list in-place, validates length.

3. **`combine_days_steps` Function**: Pairs days and steps.
    - Uses `zip` in list comprehension to create list of tuples.

💡 These tasks demonstrate list and tuple operations in mathematical and fitness contexts.

## Benefits ✅

-   Lists enable flexible, dynamic data manipulation.
-   Tuples ensure data integrity with immutability.
-   List comprehensions and `zip` simplify sequence processing.
-   Practical tasks build skills for real-world data handling.

## Recommendations 📌

-   Use list comprehensions for concise list creation.
-   Prefer tuples for immutable data to save memory.
-   Validate list lengths before operations to avoid errors.
-   Use `copy()` to avoid unintended list modifications.

## Output 📜

After completing this lesson, I now:  
✅ Create and modify lists with methods and comprehensions  
✅ Use tuples for safe, efficient data storage  
✅ Apply sequence operations like swapping and pairing  
✅ Implement solutions for fitness tracking and text processing

## Conclusion 🚀

Mastering lists and tuples enhances my ability to manage data in Python.  
From generating squares to pairing fitness data, these skills enable efficient, robust solutions for diverse programming challenges. 🧑‍💻✨
