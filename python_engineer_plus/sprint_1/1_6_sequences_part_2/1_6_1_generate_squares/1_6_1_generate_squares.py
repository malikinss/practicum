'''
TODO:
    Create a list of integers 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 using
    list comprehension.

    Use range() as the source of values.
'''
from typing import List


def generate_squares() -> List[int]:
    """
    Generate list of squares from 1 to 100.

    Returns:
        List of squares [1, 4, 9, ..., 100].
    """
    return [n**2 for n in range(1, 11)]


squares = generate_squares()
print(squares)
