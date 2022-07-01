# Resources Imports.
from resources.joke import Joke, JokeList
from resources.math import Math


def initialize_routes(api):
    # Joke Urls
    api.add_resource(JokeList, '/joke')
    api.add_resource(Joke, '/joke/<joke_type>')

    # Math Urls
    api.add_resource(Math, '/math')
