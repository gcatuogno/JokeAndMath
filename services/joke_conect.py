# Flask Imports.
from flask_restful import abort

# Imports.
import requests
import random

# Define URLS
URL_CHUCK = 'https://api.chucknorris.io/jokes/random'
URL_DAD = 'https://icanhazdadjoke.com/slack'


def joke_select(joke_type):
    """Joke Selector
        This Fuction select which joke return depending on the parameter.


    Args:
        joke_type (str): Type of Joke, Values 'Chuck' or 'Dad'

    Returns:
        str: Joke
    """
    if joke_type == 'Chuck':
        return chuck_joke()

    if joke_type == 'Dad':
        return dad_joke()

    return abort(404, message="Type {} doesn't exist".format(joke_type))


def random_joke():
    """Random Joker Selector
        This fuction return a random joke from any api
    Returns:
        str: Random Joke
    """
    joke_list = [chuck_joke(), dad_joke()]
    return random.choice(joke_list)


def chuck_joke():
    """Chuck Norris Joke 
        This fuction return a joke of Chuck Norris from the api
    Returns:
        str: Joke Chuck
    """
    data = requests.get(URL_CHUCK)
    data = data.json()
    return {'joke': data['value']}


def dad_joke():
    """Dad Joke
        This fuction return a joke of Dad from the api
    Returns:
        str: Joke Dad
    """
    data = requests.get(URL_DAD)
    data = data.json()
    return {'joke': data['attachments'][0]['text']}
