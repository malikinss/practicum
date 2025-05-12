'''
TODO:
    The message to the user has become long, hard to read, and doesn't fit on
    the tracker screen.

    Format the message: print it line by line: one parameter - one line:
        Today you have walked 1000 steps.
        Distance covered is 6.5 km.
        You have burned 330.75 kcal.
        Excellent result! Goal achieved

    Declaring a string in triple quotes will help you: f-strings work with
    this format too.
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


def get_congratulation(distance: float) -> str:
    """
    Get congratulation message based on distance.

    Args:
        distance: Distance traveled in kilometers.

    Returns:
        Congratulation message.
    """
    # Select congratulation based on distance
    if distance >= 6.5:
        return "Excellent result! Goal achieved."
    if distance >= 3.9:
        return "Not bad! The day was productive."
    if distance >= 2:
        return "Not enough, but we'll make up for it tomorrow!"
    return (
        "Lying down is also useful. "
        "The main thing is participation, not victory!"
    )


def print_stats(
    distance: float, calories: float, congratulation: str, steps: int
) -> None:
    """
    Print fitness stats line by line.

    Args:
        distance: Distance traveled in kilometers.
        calories: Kilocalories spent.
        congratulation: Congratulation message.
        steps: Number of steps taken.

    Returns:
        None, prints formatted stats.
    """
    print(
        f'Today you have walked {steps} steps.',
        f'Distance covered is {distance} km.',
        f'You have burned {calories} kcal.',
        congratulation,
        sep='\n'
    )


steps, weight, height, hours = get_fitness_data()
distance = convert_to_km(steps)
calories = calculate_calories(weight, height, distance, hours)
congratulation = get_congratulation(distance)
print_stats(distance, calories, congratulation, steps)
