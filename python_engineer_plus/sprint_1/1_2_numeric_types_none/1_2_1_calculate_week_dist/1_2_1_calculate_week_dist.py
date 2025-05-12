'''
TODO:
    The fitness tracker receives data on the distance the user has walked
    daily.

    Calculate the distance the user has walked in a week and store it in
    the variable `week_dist`.

    This is not a simple addition problem: Python does not always round
    fractional numbers correctly.

    Your goal is to avoid this problem.
'''
from decimal import Decimal
from typing import List


def calculate_week_dist(days: List[float]) -> float:
    """
    Calculate total distance walked in a week.

    Args:
        days: List of daily distances.

    Returns:
        Total distance as float with 3 decimal places.
    """
    # Sum distances using Decimal for precision
    total = sum(Decimal(str(day)) for day in days)
    return round(float(total), 3)


day_1 = 1.434
day_2 = 2.12
day_3 = 1.632
day_4 = 5.59
day_5 = 2.542
day_6 = 1.1
day_7 = 1.324

days = [day_1, day_2, day_3, day_4, day_5, day_6, day_7]
week_dist = calculate_week_dist(days)
print(week_dist)
