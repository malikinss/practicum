# Lesson 1.7: Sets 🧮

## Description 📝

This lesson covers:

-   Sets: mutable, unordered collections of unique, hashable objects
-   Creating and manipulating sets with methods and operators
-   Set operations: intersection, union, difference, symmetric difference

This lesson includes a detailed theoretical explanation, 2 programming practical tasks, and no theoretical questions, emphasizing practical set operations.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand sets and their unique, unordered nature  
✅ Perform set operations like adding, removing, and combining elements  
✅ Apply sets to tasks like duplicate removal and data processing  
✅ Solve practical problems such as text analysis and ID deduplication

## Concepts & Theory 🔍

### 🔹 Sets

-   **Purpose**: Store unique, hashable elements without order.
-   **Features**: Mutable, no duplicates, no indexing; supports fast membership tests.
-   **Creation**: Literal `{}`, `set(iterable)`; empty set via `set()`.

### 🔹 Set Operations

-   **Membership**: `in` for fast element checks.
-   **Add/Remove**: `add()`, `remove()`, `discard()`, `pop()`, `clear()`.
-   **Set Operations**:
    -   Intersection (`&`, `intersection()`): Common elements.
    -   Union (`|`, `union()`): All elements.
    -   Difference (`-`, `difference()`): Elements in one set but not another.
    -   Symmetric Difference (`^`, `symmetric_difference()`): Elements in exactly one set.

## Practical Task 🧪

### 1️⃣ **Set Manipulation**

The lesson includes 2 practical tasks applying sets:

1. **`unique_chars` Function**: Counts unique characters in a string.

    - Removes spaces, uses `set` for unique characters, returns length.

2. **`process_client_ids` Function**: Deduplicates and sorts client IDs.
    - Processes space-separated IDs, reports duplicates, returns sorted list.

💡 These tasks demonstrate sets for efficient duplicate removal and data cleaning.

## Benefits ✅

-   Sets automatically eliminate duplicates, simplifying data processing.
-   Fast membership tests optimize performance.
-   Set operations enable concise solutions for intersection and difference tasks.
-   Practical tasks build skills for text and data analysis.

## Recommendations 📌

-   Use `discard()` over `remove()` to avoid `KeyError`.
-   Prefer sets for duplicate removal and membership tests.
-   Ensure elements are hashable to avoid `TypeError`.
-   Use methods like `union()` for flexibility with iterables.

## Output 📜

After completing this lesson, I now:  
✅ Create and manipulate sets for unique data storage  
✅ Perform set operations like intersection and union  
✅ Apply sets to practical tasks like deduplication and text analysis  
✅ Implement efficient solutions for data processing

## Conclusion 🚀

Mastering sets empowers me to handle unique data efficiently in Python.  
From counting unique characters to processing client IDs, sets provide powerful tools for streamlined data manipulation in real-world applications. 🧑‍💻✨
