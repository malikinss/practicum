'''
TODO:
    Calorie counting is a standard feature of fitness trackers, and
    the "runaway" tracker from Unicorn is no exception.

    Consumption can be calculated using different algorithms, and Unicorn took
    the formula developed by scientists at Southern Methodist University
    in Dallas.

    The formula states: kilocalorie expenditure per minute of movement
    is equal to the sum of:
        - 0.035 of the user's weight
        - and the product of two values:
            1. the square of the speed in km/h, divided by the user's height;
            2. 0.029 of the user's weight.

    Write a formula that calculates kilocalorie expenditure over two hours.
'''
from decimal import Decimal


def calculate_calories(
    weight: float,
    height: float,
    dist: float,
    hours: float
) -> float:
    """
    Calculate kilocalories spent over a period.

    Args:
        weight: User's weight in kg.
        height: User's height in cm.
        dist: Distance traveled in km.
        hours: Duration in hours.

    Returns:
        Kilocalories spent, rounded to 2 decimal places.
    """
    # Calculate speed in km/h
    speed = Decimal(str(dist)) / Decimal(str(hours))
    minutes = Decimal(str(hours)) * 60
    calories_per_min = (
        Decimal('0.035') * Decimal(str(weight)) +
        (speed ** 2 / Decimal(str(height))) *
        Decimal('0.029') * Decimal(str(weight))
    )
    return round(float(calories_per_min * minutes), 2)


weight = 75
height = 175
dist = 9.75
hours = 2
spent_calories = calculate_calories(weight, height, dist, hours)
print(spent_calories)
