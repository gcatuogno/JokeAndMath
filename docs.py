# Resources Imports.
from resources.joke import Joke, JokeList
from resources.math import Math


def initialize_docs(docs):
    # Joke Urls
    docs.register(Joke)
    docs.register(JokeList)

    docs.register(Math)
