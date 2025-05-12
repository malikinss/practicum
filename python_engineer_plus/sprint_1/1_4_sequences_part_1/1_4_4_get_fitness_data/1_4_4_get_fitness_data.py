'''
TODO:
    It's time to teach the fitness tracker to output information messages and
    calculation results.

    The software module accepts the number of steps as input, but the distance
    traveled by the user is then described in kilometers.

    Teach the program to convert steps to kilometers.

    After the calculations, the program should print two numbers separated by
    a space on one line: the distance traveled in kilometers and the number
    of kilocalories burned; for example:
        10.54 685
'''
from decimal import Decimal
from typing import Tuple


STEP_LENGTH_M = 0.65


def calculate_calories(
    weight: float, height: float, dist: float, hours: float
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
    speed = Decimal(str(dist)) / Decimal(str(hours))
    minutes = Decimal(str(hours)) * 60
    calories_per_min = (
        Decimal('0.035') * Decimal(str(weight)) +
        (speed ** 2 / Decimal(str(height))) *
        Decimal('0.029') * Decimal(str(weight))
    )
    return round(float(calories_per_min * minutes), 2)


def convert_to_km(steps: int) -> float:
    """
    Convert steps to kilometers.

    Args:
        steps: Number of steps taken.

    Returns:
        Distance in kilometers, rounded to 2 decimal places.
    """
    return round(float((steps * STEP_LENGTH_M) / 1000), 2)


def get_fitness_data() -> Tuple[int, float, float, float]:
    """
    Get fitness data from user input.

    Returns:
        Tuple of (steps, weight, height, hours).
    """
    steps = int(input("Enter number of steps: "))
    return steps, 75.0, 175.0, 2.0


steps, weight, height, hours = get_fitness_data()
distance = convert_to_km(steps)
calories = calculate_calories(weight, height, distance, hours)
print(f"{distance:.2f} {calories:.2f}")
