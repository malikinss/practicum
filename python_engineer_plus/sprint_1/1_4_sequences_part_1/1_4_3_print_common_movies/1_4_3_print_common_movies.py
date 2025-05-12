'''
TODO:
The variable `recommended_movies` stores a list of recommended movies,
and `hackers_movies` stores a list of "Top 12 Movies About Coders and Hackers".

Print only those recommended movies that are in the top list to the terminal.

For each movie, the line:
    `We recommend that programmers watch the movie "<movie_name>"`
should be printed.
'''
from typing import List


def print_common_movies(
    recommended: List[str], hackers: List[str]
) -> None:
    """
    Print recommended movies that are in hackers list.

    Args:
        recommended: List of recommended movies.
        hackers: List of top hacker movies.

    Returns:
        None, prints recommendations to console.
    """
    # Filter and print common movies
    for movie in recommended:
        if movie in hackers:
            print(
                f'We recommend that programmers watch the movie '
                f'"{movie}"'
            )


recommended_movies = [
    'Hatiko', '23', 'Knocking on Heaven Doors',
    'Hackers', 'Trone', '1408'
]
hacker_movies = [
    'Trone', 'War Games', 'Sneakers',
    'Jonny Mnemonik', 'Hackers', 'Nirvana',
    '23', 'Who Am I', 'Net',
    'Sword Fish', 'Enemy of the State', 'Takedown'
]
print_common_movies(recommended_movies, hacker_movies)
