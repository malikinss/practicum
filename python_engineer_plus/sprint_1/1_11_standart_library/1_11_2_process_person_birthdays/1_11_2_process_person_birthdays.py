'''
TODO:
    Create a program that determines how many days are left until the birthday
    of a list of people.

    The program uses the `datetime` module and takes into account whether
    the birthday has passed in the current year.

    Input:
        - A list of `people` tuples, where each tuple contains:
            - `name` (string) — the person's name.
            - `date_birthday` (string) — the birth date in the format
                                         "DD.MM.YYYY".

    Output:
        - For each person in the list, print the string:
            <name>, days left until your birthday: <days_until_birthday>
            logic.
'''
import datetime as dt
from typing import List, Tuple


def parse_date(date_str: str) -> dt.date:
    """
    Parse date string in DD.MM.YYYY format.

    Args:
        date_str: Date string in DD.MM.YYYY format.

    Returns:
        Parsed date object.

    Raises:
        ValueError: If date format is invalid.
    """
    # Parse date string
    try:
        return dt.datetime.strptime(date_str, "%d.%m.%Y").date()
    except ValueError as e:
        raise ValueError(f"Invalid date format: {date_str}") from e


def days_to_birthday(birthday: dt.date, current_date: dt.date) -> int:
    """
    Calculate days until the next birthday.

    Args:
        birthday: Date of birth.
        current_date: Current date.

    Returns:
        Number of days until the next birthday.
    """
    # Calculate next birthday
    next_birthday = dt.date(
        current_date.year, birthday.month, birthday.day
    )
    if next_birthday < current_date:
        next_birthday = dt.date(
            current_date.year + 1, birthday.month, birthday.day
        )
    return (next_birthday - current_date).days


def process_person_birthdays(persons: List[Tuple[str, str]]) -> None:
    """
    Process birthdays and print days until next birthday.

    Args:
        persons: List of (name, date_birthday) tuples.

    Returns:
        None, prints days until each birthday.
    """
    current_date = dt.datetime.now().date()
    for name, b_date_str in persons:
        try:
            b_date = parse_date(b_date_str)
            days = days_to_birthday(b_date, current_date)
            print(f"{name}, days left until your birthday: {days}")
        except ValueError as e:
            print(f"Error for {name}: {e}")


process_person_birthdays([("Lera", "16.05.2015"), ("Maxim", "16.12.2011")])
