# Flask Imports
from flask_unittest import ClientTestCase
from flask.testing import FlaskClient

# App Import
from app import app


class Joke_test(ClientTestCase):
    """Joke Test
        Class to test all function of Joke.
    """

    # Declare app.
    app = app

    def test_random_joke(self, client: FlaskClient):
        """Test Random Joke
        This Fuction test a random joke endpoint.
        """
        response = client.get(
            '/joke')

        result = response.data
        result = result.decode('UTF-8')
        self.assertIn('joke', result, msg='[-] JOKE NOT FOUND!!')

    def test_chuck_joke(self, client: FlaskClient):
        """Test Chuck Joke
        This Fuction test a Chuck joke endpoint.
        """
        response = client.get(
            '/joke/Chuck')

        result = response.data
        result = result.decode('UTF-8')
        self.assertIn('joke', result, msg='[-] JOKE NOT FOUND!!')

    def test_dad_joke(self, client: FlaskClient):
        """Test Dad Joke
        This Fuction test a Dad joke endpoint.
        """
        response = client.get(
            '/joke/Dad')

        result = response.data
        result = result.decode('UTF-8')
        self.assertIn('joke', result, msg='[-] JOKE NOT FOUND!!')

    def test_new_joke(self, client: FlaskClient):
        """Test New Joke
        This Fuction test a New joke endpoint.
        """
        response = client.post(
            '/joke', data={
                'joke': 'test joke'
            })

        self.assertEqual(response.status, '201 CREATED')

    def test_put_joke(self, client: FlaskClient):
        """Test Modify Joke
        This Fuction test a Modify joke endpoint.
        """
        response = client.put(
            '/joke', data={
                'number': 1,
                'joke': 'Change Joke'
            })
        self.assertEqual(response.status, '200 OK')

    def test_delete_joke(self, client: FlaskClient):
        """Test Delete Joke
        This Fuction test a Modify joke endpoint.
        """
        response = client.delete(
            '/joke', headers={
                'number': 1
            })
        self.assertEqual(response.status, '200 OK')

    def test_error_path(self, client: FlaskClient):
        """Test error path
        This Fuction test a Modify joke endpoint.
        """
        response = client.get(
            '/joke/dad')

        self.assertEqual(response.status, '404 NOT FOUND')
