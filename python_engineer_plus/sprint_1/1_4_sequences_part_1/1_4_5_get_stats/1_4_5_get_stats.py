'''
TODO:
    Thanks to your work, the fitness tracker module can already count distance
    and calories, but a modern user will not be impressed by the output of
    incomprehensible numbers on the screen.

    Edit the code so that the print() function returns the following string:
        Today you walked <distance_in_km> km and spent <number_of_kilocalories>
        kilocalories.

    Instead of <distance_in_km> and <number_of_kilocalories>, numeric values
    should be substituted.

    Output the values of the distance traveled and kilocalories spent rounded
    to hundredths.

    Use f-strings in the solution.
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


def get_stats(distance: float, calories: float) -> str:
    """
    Format fitness stats as a message.

    Args:
        distance: Distance traveled in kilometers.
        calories: Kilocalories spent.

    Returns:
        Formatted message with distance and calories.
    """
    return (
        f"Today you walked {distance:.2f} km and spent "
        f"{calories:.2f} kilocalories."
    )


steps, weight, height, hours = get_fitness_data()
distance = convert_to_km(steps)
calories = calculate_calories(weight, height, distance, hours)
print(get_stats(distance, calories))
