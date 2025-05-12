'''
TODO:
    The function takes as arguments the initial and final values of the range
    and an undefined number of numbers to check.

    Write a function that will return a list of numbers that fall within
    the specified range.

    If the value is outside the range, the function should print the message:
        "Number out of range".

    Add the function test_range() so that it:
        - takes as arguments:
            - the initial and final values of the range,
            - an undefined number of numbers to check;
        - forms a list of numbers that fall within the specified range;
        - for values that are outside the range, prints the message:
            "Number out of range";
        - returns a list of numbers that fall within the specified range.
'''
from typing import List, Union


def test_range(
    start: Union[int, float], stop: Union[int, float], *args: Union[int, float]
) -> List[Union[int, float]]:
    """
    Filter numbers within a specified range.

    Args:
        start: Start of the range (inclusive).
        stop: End of the range (exclusive).
        *args: Numbers to check.

    Returns:
        List of numbers within [start, stop).
    """
    # Check numbers and collect those in range
    in_range = []
    for num in args:
        if not isinstance(num, (int, float)):
            print('Number out of range')
            continue
        if start <= num < stop:
            in_range.append(num)
        else:
            print('Number out of range')
    return in_range


# Example usage
print(test_range(2, 8, 1, 3, 7, 9))
