# print_common_movies Function Implementation

## Description 📝

The provided code implements the `print_common_movies` function, which identifies and prints movies that appear in both the `recommended_movies` list and the `hacker_movies` list (top 12 movies about coders and hackers).
For each common movie, it prints a formatted message: `We recommend that programmers watch the movie "<movie_name>"`.
The function uses a simple loop to check for common elements and prints the required message for each match.
The code then applies this function to the provided lists and outputs the results.

## Purpose 🎯

Intended for filtering and displaying common elements between two lists, such as movie recommendation systems, data processing, or educational examples of list operations and string formatting in Python.

## How It Works 🔍

-   **Function Definition**:
    -   `print_common_movies` takes two parameters:
        -   `recommended`: A list of recommended movie titles (strings).
        -   `hackers`: A list of top hacker movie titles (strings).
    -   Returns `None`, printing messages to the console.
    -   Uses type hints (`List[str]`) for clarity.
-   **Processing**:
    -   Iterates over each movie in `recommended`.
    -   Checks if the movie is in `hackers` using the `in` operator.
    -   If a match is found, prints the formatted message:
        -   `f'We recommend that programmers watch the movie "{movie}"'`.
-   **Main Code**:
    -   Defines two lists:
        -   `recommended_movies = ['Hatiko', '23', 'Knocking on Heaven Doors', 'Hackers', 'Trone', '1408']`.
        -   `hacker_movies = ['Trone', 'War Games', 'Sneakers', 'Jonny Mnemonik', 'Hackers', 'Nirvana', '23', 'Who Am I', 'Net', 'Sword Fish', 'Enemy of the State', 'Takedown']`.
    -   Calls `print_common_movies(recommended_movies, hacker_movies)`.
-   **Behavior**:
    -   Identifies common movies: `'23'`, `'Hackers'`, `'Trone'`.
    -   Prints for each:
        ```
        We recommend that programmers watch the movie "23"
        We recommend that programmers watch the movie "Hackers"
        We recommend that programmers watch the movie "Trone"
        ```
    -   Only prints movies from `recommended_movies` that are also in `hacker_movies`.
    -   Maintains the order of movies as they appear in `recommended_movies`.

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:
    -   Prints only movies that are in both `recommended_movies` and `hacker_movies`.
    -   Common movies:
        -   `'23'` (in both lists).
        -   `'Hackers'` (in both lists).
        -   `'Trone'` (in both lists).
    -   Output:
        ```
        We recommend that programmers watch the movie "23"
        We recommend that programmers watch the movie "Hackers"
        We recommend that programmers watch the movie "Trone"
        ```
-   **Format**:
    -   Each line follows the exact format:
        -   `We recommend that programmers watch the movie "<movie_name>"`.
    -   Movie names are enclosed in quotes.
-   **Correctness**:
    -   Checks for membership using `movie in hackers`, which is case-sensitive and exact.
    -   Only iterates over `recommended`, ensuring only recommended movies are printed.
    -   Preserves order from `recommended_movies` (`'23'`, `'Hackers'`, `'Trone'`).
    -   No validation needed, as inputs are guaranteed to be lists of strings.
-   **Documentation**: Clear docstring with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `in` operator correctly identifies exact string matches.
    -   Common movies (`'23'`, `'Hackers'`, `'Trone'`) are printed in the order they appear in `recommended_movies`.
    -   Formatted string (`f-string`) ensures quotes around movie names and exact message wording.
    -   No duplicates in `recommended_movies`, so no special handling needed.
-   **Performance**:
    -   Iteration over `recommended`: O(n), where n is the length of `recommended` (n=6).
    -   Membership check `movie in hackers`: O(m), where m is the length of `hackers` (m=12).
    -   Total: O(n _ m), or O(6 _ 12) = O(72) for the given inputs.
    -   Efficient for small lists like those provided.
-   **Design**:
    -   Type hints (`List[str]`) clarify input types.
    -   Simple loop and condition are clear and maintainable.
    -   F-string formatting ensures readable output.
    -   Returns `None`, as the task requires printing, not returning values.
-   **Alternatives**:
    -   Set intersection: `set(recommended) & set(hackers)` is faster (O(min(n, m))), but loses order from `recommended`.
    -   List comprehension: Less clear for printing directly.
    -   Manual comparison: More complex and error-prone.
-   **Extensibility**:
    -   Easily modified to return a list of common movies instead of printing.
    -   Could add case-insensitive matching or partial matching if needed.
-   **Edge Cases**:
    -   Empty `recommended`: Prints nothing.
    -   Empty `hackers`: Prints nothing (no matches).
    -   No common movies: Prints nothing (e.g., `recommended=['Hatiko']`).
    -   Case sensitivity: Matches exact strings, as required (e.g., `'Trone'` ≠ `'trone'`).
    -   Duplicates: Not present in provided lists, but would print duplicates if in `recommended`.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Provided example
recommended_movies = [
    'Hatiko', '23', 'Knocking on Heaven Doors',
    'Hackers', 'Trone', '1408'
]
hacker_movies = [
    'Trone', 'War Games', 'Sneakers',
    'Jonny Mnemonik', 'Hackers', 'Nirvana',
    '23', 'Who Am I', 'Net',
    'Sword Fish', 'Enemy of the State', 'Takedown'
]
print_common_movies(recommended_movies, hacker_movies)
# Output:
# We recommend that programmers watch the movie "23"
# We recommend that programmers watch the movie "Hackers"
# We recommend that programmers watch the movie "Trone"

# Additional test cases
print_common_movies(['Hatiko', '1408'], hacker_movies)
# Output: (nothing, no common movies)

print_common_movies(['23', '23'], hacker_movies)
# Output:
# We recommend that programmers watch the movie "23"
# We recommend that programmers watch the movie "23"

print_common_movies([], hacker_movies)
# Output: (nothing, empty recommended list)

print_common_movies(recommended_movies, ['Other'])
# Output: (nothing, no common movies)
```

## Conclusion 🚀

The `print_common_movies` function implementation is precise, correctly identifying and printing the common movies `'23'`, `'Hackers'`, and `'Trone'` from the provided lists in the required format.
It uses a simple and efficient loop with membership checks, maintains the order from `recommended_movies`, and formats output exactly as specified.
The implementation is robust, extensible, and ideal for list filtering tasks or teaching list operations, fully compliant with the task’s requirements.
