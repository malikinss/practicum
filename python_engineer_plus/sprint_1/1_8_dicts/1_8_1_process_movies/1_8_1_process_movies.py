'''
TODO:
    The online movie theater sends Anton a list of movies recommended for
    viewing.

    Help Anton choose movies with a high rating and add them to his favorites.

    If a recommended movie has a rating lower than 4.0, remove it from
    the recommended_movie dictionary.

    The program should display the following message:
        The movie "<movie_name>" is not interesting: "<review_of_the_movie>".
        The movie has been removed from the recommendations.

    The program should add all movies with a rating higher than 4.0 to
    the favorites_movie dictionary and display the following message:
        The movie "<movie_name>" has a good review: "<review_of_the_movie>".
        The movie has been added to your favorites.

    Print the resulting collection of favorite movies.
'''
from typing import Dict, TypedDict


class MovieInfo(TypedDict):
    rating: float
    review: str


def process_movies(
    recommended: Dict[str, MovieInfo],
    favorites: Dict[str, MovieInfo]
) -> None:
    """
    Process recommended movies and update favorites.

    Args:
        recommended: Dict of movies with rating and review.
        favorites: Dict to store high-rated movies.

    Returns:
        None, modifies dictionaries and prints messages.
    """
    to_remove = []
    for title, info in recommended.items():
        rating = info['rating']
        review = info['review']
        if rating < 4.0:
            to_remove.append(title)
            print(
                f'The movie "{title}" is not interesting: "{review}".\n'
                f'The movie has been removed from the recommendations.'
            )
        else:
            favorites[title] = info
            print(
                f'The movie "{title}" has a good review: "{review}".\n'
                f'The movie has been added to your favorites.'
            )

    for title in to_remove:
        recommended.pop(title)


favorites_movie: Dict[str, MovieInfo] = {}
recommended_movie: Dict[str, MovieInfo] = {
    'Hancock': {'rating': 4.5, 'review': 'You can watch it'},
    'Matrix': {'rating': 4.7, 'review': 'the movie is cool'},
    'Cyber': {'rating': 2.5, 'review': 'so-so movie'},
    'Trone': {'rating': 3.8, 'review': 'so-so movie'},
    'Avengers': {'rating': 4.7, 'review': 'the movie is cool'},
    'Hackers': {'rating': 4.5, 'review': 'You can watch it'}
}

process_movies(recommended_movie, favorites_movie)
print(favorites_movie)
