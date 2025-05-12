'''
TODO:
    Assemble and print the phrase "ты программист" from the strings a, b and c
    using slices with two and three parameters.

    The phrase must begin with a lowercase letter.
'''
from typing import Tuple


def build_phrase(strings: Tuple[str, str, str]) -> str:
    """
    Build phrase 'ты программист' from input strings using slices.

    Args:
        strings: Tuple of three input strings.

    Returns:
        Phrase 'ты программист'.

    Raises:
        ValueError: If any string is too short.
    """
    a, b, c = strings
    if len(a) < 9 or len(b) < 5 or len(c) < 7:
        raise ValueError("Input strings too short")
    # Assemble phrase using two- and three-parameter slices
    return (a[4:6] + b[2:5:2] + c[2:7] + c[1:4:2] + a[7:9])


a = 'Роботы стали важны'
b = 'в период'
c = 'эмиграции с Терры'
result = build_phrase((a, b, c))
print(result)
