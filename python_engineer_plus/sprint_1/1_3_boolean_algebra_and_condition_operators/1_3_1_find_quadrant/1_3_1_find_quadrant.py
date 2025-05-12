'''
TODO:
    Write a program that, when launched, receives x and y values,
    the coordinates of a point on a plane.

    The program must determine in which quadrant of the coordinate plane
    the point with the given coordinates is located.
'''
from typing import Tuple


def find_quadrant(x: float, y: float) -> str:
    """
    Determine the quadrant of a point on the coordinate plane.

    Args:
        x: X-coordinate of the point.
        y: Y-coordinate of the point.

    Returns:
        Quadrant name or indication that point is on an axis.
    """
    # Check if point lies on an axis
    if x == 0 or y == 0:
        return "Point on axis"
    if x > 0 and y > 0:
        return "First Quadrant"
    if x < 0 and y > 0:
        return "Second Quadrant"
    if x < 0 and y < 0:
        return "Third Quadrant"
    return "Fourth Quadrant"


def get_coordinates() -> Tuple[float, float]:
    """
    Get x and y coordinates from user input.

    Returns:
        Tuple of (x, y) coordinates.
    """
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))
    return x, y


x, y = get_coordinates()
print(find_quadrant(x, y))
