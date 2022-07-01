# Flask Imports
from flask_unittest import ClientTestCase
from flask.testing import FlaskClient

# App Import
from app import app


class Math_test(ClientTestCase):
    """Math Test
        Class to test all function of Math.
    """

    # Declare app.
    app = app

    def test_mcm(self, client: FlaskClient):
        """Test MCM Function
        This Fuction test a MCM fuction endpoint.
        """
        response = client.get(
            '/math', data={
                'numbers': '1,2,5,8,7,9'
            })

        self.assertEqual(response.status, '200 OK')

    def test_sum(self, client: FlaskClient):
        """Test Sum Function
        This Fuction test a Sum fuction endpoint.
        """
        response = client.get(
            '/math', data={
                'number': '1000'
            })

        self.assertEqual(response.status, '200 OK')
