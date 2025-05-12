'''
TODO:
    The time tracking system saves the time employees spent on social networks
    per month on the server.

    HR decided to find out how much time tester Anton spent scrolling through
    the feed with memes, but the server returned an incomprehensible number:
        `424562`.

    HR read the manuals for the system and found out that the server saves
    time in seconds.

    HR asked you to write an application that would use arithmetic operations
    to convert the received number of seconds into the `days hours minutes
    seconds` format.

    Why not help a good person.
'''
from typing import Tuple


def convert_seconds(seconds: int) -> Tuple[int, int, int, int]:
    """
    Convert seconds to days, hours, minutes, seconds.

    Args:
        seconds: Total seconds to convert.

    Returns:
        Tuple of (days, hours, minutes, seconds).
    """
    sec_per_minute = 60
    sec_per_hour = sec_per_minute * 60
    sec_per_day = sec_per_hour * 24

    # Calculate days and remaining seconds
    days = seconds // sec_per_day
    seconds -= days * sec_per_day

    hours = seconds // sec_per_hour
    seconds -= hours * sec_per_hour

    minutes = seconds // sec_per_minute
    seconds -= minutes * sec_per_minute

    return days, hours, minutes, seconds


response = 424562
days, hours, minutes, seconds = convert_seconds(response)
print(days, hours, minutes, seconds)
