'''
TODO:
    Find the number of unique characters in a string, excluding spaces.
'''


def unique_chars(text: str) -> int:
    """
    Count unique characters in a string, excluding spaces.

    Args:
        text: Input string.

    Returns:
        Number of unique characters (excluding spaces).
    """
    return len(set(text.replace(' ', '')))
