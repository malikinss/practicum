from math import sqrt


def calculate_square_root(number):
    """
    Calculates the square root of a given number.

    Args:
        number (float): The number to calculate the square root for.

    Returns:
        float: The square root of the given number.
    """
    return sqrt(number)


def calc(your_number):
    """
    Calculates the square root of a user-defined number.

    Args:
        your_number (float): The number for which the square root will
        be calculated.

    Prints:
        string: A message indicating the calculated square root.
    """
    if your_number <= 0:
        return

    root = calculate_square_root(your_number)

    print(f'We calculate the square root of your given number. '
          f"It'll be {root}")


message = ('Welcome to the best software for '
           'square root calculation for a given number')

print(message)

calc(25.5)
