'''
TODO:
    Cast the variables to the required type, perform the necessary operations
    on them, pass the values to the f-string and print the phrase:
        The sum of the numbers 1, 2 and 3 is 6
'''
from typing import List, Union


def sum_numbers(a: int, b: str, c: List[Union[str, float]]) -> str:
    """
    Sum numbers and format result as a string.

    Args:
        a: First number (integer).
        b: Second number (string representation).
        c: List containing a string with the third number.

    Returns:
        Formatted string with the sum of numbers.
    """
    # Extract and sum numbers, format result
    c_value = int(c[2].split()[0])  # type: ignore
    total = a + int(b) + c_value
    return f"The sum of the numbers {a}, {b} and {c_value} is {total}"


a = 1
b = '2'
c: List[Union[str, float]] = ['Antony', 3.15, '3 piglets']
print(sum_numbers(a, b, c))
