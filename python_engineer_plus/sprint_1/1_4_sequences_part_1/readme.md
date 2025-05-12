# Lesson 1.4: Sequences, Loops, and Strings 🔄

## Description 📝

This lesson covers:

-   Collections and sequences (`list`, `tuple`, `range`, `str`)
-   Sequence operations (indexing, slicing, comparison, etc.)
-   Loops (`while`, `for`) for iterating over sequences
-   String manipulation and formatting

This lesson includes a detailed theoretical explanation, 7 programming practical tasks, and no theoretical questions, emphasizing hands-on practice with sequences and loops.

## Purpose 🎯

By the end of this lesson, I will:  
✅ Understand and manipulate sequences like lists, strings, and ranges  
✅ Use loops to process sequences efficiently  
✅ Apply string methods and formatting for text processing  
✅ Solve practical problems like fitness tracking and movie recommendations

## Concepts & Theory 🔍

### 🔹 Collections and Sequences

-   **Collections**: Group related data in one variable.
-   **Sequences**: Ordered collections (`list`, `tuple`, `range`, `str`) accessible by index.
-   **Non-Ordered**: Unordered collections like sets.

### 🔹 Sequence Operations

-   **Indexing**: Access elements by index (0-based); `IndexError` for invalid indices.
-   **Comparison**: Element-by-element, Unicode-based for strings.
-   **Min/Max**: `min()`, `max()` for homogeneous sequences.
-   **Concatenation/Repetition**: `+` for joining, `*` for repeating.
-   **Length**: `len()` for element count.
-   **Membership**: `in`/`not in` for checking presence.
-   **Slicing**: `sequence[start:end:step]` for subsequences.

### 🔹 Loops

-   **While**: Repeats while condition is `True`.
-   **For**: Iterates over elements of an iterable.
-   **Range**: Generates number sequences with `range(start, stop, step)`.

### 🔹 Strings

-   **Definition**: Text sequences in single, double, or triple quotes.
-   **Methods**: `lower()`, `upper()`, `find()`, `replace()`, `strip()`, `split()`, `join()`.
-   **Formatting**: `format()`, f-strings (e.g., `f'Text {variable}'`).
-   **PEP8**: Max line length 79 characters.

## Practical Task 🧪

### 1️⃣ **Sequence and String Processing**

The lesson includes 7 practical tasks applying sequences, loops, and strings:

1. **`print_word_from_string` Function**: Extracts "Домик" from a string.

    - Prints characters at specific indices, validates string length.

2. **`build_phrase` Function**: Builds "ты программист" from slices.

    - Uses string slicing, validates input length.

3. **`print_common_movies` Function**: Finds common movies in lists.

    - Prints formatted recommendations for shared movies.

4. **`get_fitness_data` Function**: Converts steps to km and calories.

    - Outputs distance and calories with fixed parameters.

5. **`get_stats` Function**: Formats fitness stats.

    - Outputs steps, distance, and calories in a single string.

6. **`get_congratulation` Function**: Adds motivational message.

    - Selects congratulation based on distance thresholds.

7. **`print_stats` Function**: Multi-line fitness output.
    - Prints steps, distance, calories, and congratulation per line.

💡 These tasks demonstrate sequence manipulation, looping, and string formatting in fitness and text applications.

## Benefits ✅

-   Sequences simplify data management with indexing and slicing.
-   Loops reduce code repetition, adhering to DRY principles.
-   String methods and formatting enhance text processing.
-   Practical tasks build skills for real-world applications like fitness tracking.

## Recommendations 📌

-   Use f-strings for readable string formatting.
-   Validate sequence lengths to avoid `IndexError`.
-   Follow PEP8 for line length and code clarity.
-   Prefer `for` loops for iterables, `while` for condition-based repetition.

## Output 📜

After completing this lesson, I now:  
✅ Manipulate lists, strings, and ranges with sequence operations  
✅ Use loops to process data efficiently  
✅ Apply string methods and formatting for text tasks  
✅ Implement fitness tracking and text processing solutions

## Conclusion 🚀

Mastering sequences, loops, and strings equips me to handle data and text effectively in Python.  
From building fitness trackers to processing movie lists, these skills enable practical, efficient programming solutions. 🧑‍💻✨
