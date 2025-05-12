'''
TODO:
    From a tuple and a list, create a list of tuples.

    The program receives:
        - a days tuple with a list of days of the week,
        - a steps list, which lists the number of steps the user took on
          the corresponding day; for example:
            steps[0] is the number of steps on Monday.

    The program should return a list of tuples, each containing two elements:
        the name of the day of the week and the number of steps for that day.
'''
from typing import List, Tuple


def combine_days_steps(
    days: Tuple[str, ...], steps: List[int]
) -> List[Tuple[str, int]]:
    """
    Combine days and steps into a list of tuples.

    Args:
        days: Tuple of weekday names.
        steps: List of step counts for each day.

    Returns:
        List of (day, steps) tuples.
    """
    return [(day, step) for day, step in zip(days, steps)]


days = ('mon', 'tue', 'wen', 'thu', 'fri', 'sat', 'sun')
steps = [1500, 3445, 13222, 10000, 12555, 1300, 6000]
result = combine_days_steps(days, steps)
print(result)
