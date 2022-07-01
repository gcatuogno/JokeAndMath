# Flask Imports
from flask import request
from flask_restful import Resource

# Fuction Imports.
from services.joke_conect import random_joke
from services.joke_conect import joke_select

# Flask ApiSpec Imports.
from flask_apispec.views import MethodResource

# Data Base Imports
# ? Uncomment dbSQLite to use this data base and comment the other.
import dbPostgress as db
# import dbSQLite as db

# Models Imports.
from models.joke_model import Joke_model


class Joke(MethodResource, Resource):
    """Joke Class.
    This Class is use to return a specific joke.    
    """

    def get(self, joke_type=None):
        """Get Joke

        Args:
            joke_type (str): Value to select a type of joke. Value 'Chuck' or 'Dad'. Defaults to None.

        Returns:
            str: Joke.
        """
        return joke_select(joke_type)


class JokeList(MethodResource, Resource):
    """Joke List
        This Class contains the methods, 
        -Random Joke.
        -New Joke.
        -Modefy Joke.
        -Delete Joke.
    """

    def get(self):
        """Get Random Joke

        Returns:
            str: Random Joke
        """
        return random_joke()

    def post(self):
        """New Joke
            This Fuction Save in database a new joke, this joke must be unique.
            No one liked repeated jokes!! :)

            The Args are send in Body.
        Args: 
            joke (str) : Text with the joke.
        Returns:
            obj: with a messaje 'Joke Saved'
        """
        data = request.form

        if not "joke" in data:
            return {'POST': 'No hay un Chiste para guardar'}

        joke = Joke_model(text=request.form['joke'])
        db.session.add(joke)
        db.session.commit()

        return {'message': 'Joke Saved'}, 201

    def put(self):
        """Modify a Joke.
        This fuction modify a existing joke.

        The Args are send in Body.
        Args: 
            number (int) : ID of the joke.
            joke (str) : Text with the joke.

        Returns:
            obj: with a messaje 'Joke Update'
        """
        joke = db.session.query(Joke_model).filter_by(
            id=request.form['number']).first()
        joke.text = request.form['joke']
        db.session.commit()
        return {'message': 'Joke Update'}

    def delete(self):
        """Delete a Joke.
        This fuction delete a existing joke.

        The Args are send in Headers.
        Args: 
            number (int) : ID of the joke.

        Returns:
            obj: with a messaje 'Joke Delete'
        """
        db.session.query(Joke_model).filter_by(
            id=request.headers['number']).delete()
        db.session.commit()
        return {'message': 'Joke Delete'}
