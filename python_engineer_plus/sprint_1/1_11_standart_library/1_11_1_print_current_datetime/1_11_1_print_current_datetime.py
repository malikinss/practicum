'''
TODO:
    Import the datetime module.

    One of the data types available in the datetime module is named exactly
    like the module itself.

    As a result, accessing this type may look like datetime.datetime(...).

    This can lead to confusion; to avoid it, rename the module when importing.

    Print the current date and time to the console.
'''
import datetime as dt


def print_current_datetime() -> None:
    """
    Print the current date and time.

    Returns:
        None, prints the current datetime.
    """
    print(dt.datetime.now())


print_current_datetime()
