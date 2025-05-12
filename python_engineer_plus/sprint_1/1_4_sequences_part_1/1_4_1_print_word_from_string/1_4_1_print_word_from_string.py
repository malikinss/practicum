'''
TODO:
    Print the elements of the string so that the output to the terminal forms
    a word:
        Д
        o
        м
        и
        к
'''


def print_word_from_string(text: str):
    """
    Print letters from string to form 'Домик'.

    Args:
        text: Input string to extract letters from.

    Raises:
        ValueError: If string is too short.
    """
    if len(text) < 11:
        raise ValueError("String too short to form 'Домик'")
    # Select letters for 'Домик'
    indices = [0, 2, 10, 4, -1]
    for i in indices:
        print(text[i])


name_movie = 'Джонни Мнемоник'
print_word_from_string(name_movie)
