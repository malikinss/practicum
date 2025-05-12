'''
TODO:
    Master Yoda has grown old and his speech has become very bad: he has
    started swapping the first and last words of his sentences.

    Write a program that can normalize his sentences.

    Without creating a new object, swap the first and last words.
'''
from typing import List


def swap_first_last(sentence: List[str]) -> None:
    """
    Swap first and last words in a sentence in-place.

    Args:
        sentence: List of words representing a sentence.

    Returns:
        None, modifies the input list in-place.
    """
    if len(sentence) >= 2:
        sentence[0], sentence[-1] = sentence[-1], sentence[0]


force_words = ['you', 'the force', 'be', 'with', 'May']
swap_first_last(force_words)
print(force_words)
