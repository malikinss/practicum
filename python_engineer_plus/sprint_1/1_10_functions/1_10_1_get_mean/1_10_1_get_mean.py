'''
TODO:
    The `get_mean()` function receives a list of numbers as input.

    Write the function code so that it returns the arithmetic mean of
    the numbers in the received list.

    Call the `get_mean()` function with the `num_lst` argument; print
    the result of the call, rounded to two decimal places.
'''
from typing import List


def get_mean(values: List[float | int]) -> float:
    """
    Calculate the arithmetic mean of a list of numbers.

    Args:
        values: List of numbers.

    Returns:
        Arithmetic mean rounded to two decimal places.
        Returns 0.0 for empty lists.
    """
    if not values:
        return 0.0
    return round(sum(values) / len(values), 2)


num_lst: list = [3, 6, 5, 7, 9, 1]
print(get_mean(num_lst))
