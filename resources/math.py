# Flask Imports.
from flask import request
from flask_restful import Resource

# Fuction Imports
from MathFuction.Fuctions import mcm, sum

from flask_apispec.views import MethodResource


class Math(MethodResource, Resource):
    """Class Math.
        In this Class are define all mathematical methods.

    """

    def get(self):
        """Get Fuction.
            This Fuction select which method to apply according to the request. 

        Returns:
            int: Least Common Multiple
            int: Number
        """
        if 'numbers' in request.form:
            mcm_number = mcm(eval(request.form['numbers']))
            return {'result': mcm_number}

        if 'number' in request.form:
            number = sum(request.form['number'])
            return {'result': number}
