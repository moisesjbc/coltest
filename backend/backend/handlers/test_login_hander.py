import json
from .app import make_app
from tornado.testing import AsyncHTTPTestCase
from unittest.mock import MagicMock
from ..authentication.authentication import Authentication

class TestLoginHandler(AsyncHTTPTestCase):
    def get_app(self):
        return make_app()

    def test_login_ok(self):
        expected_token = "generated-token"
        Authentication.generate_token = MagicMock(return_value=expected_token)

        response = self.fetch("/login", method="PUT", body=json.dumps({
            "username": "Admin",
            "password": "Admin-1234"
        }))
        response_data = json.loads(response.body)

        self.assertEqual(response.code, 200)
        self.assertEqual(response_data, {"token": expected_token})

    def test_login_invalid_username(self):
        response = self.fetch("/login", method="PUT", body=json.dumps({
            "username": "Admin-404",
            "password": "Admin-1234"
        }))
        response_data = json.loads(response.body)

        self.assertEqual(response.code, 401)
        self.assertEqual(response_data, {"cause": "Invalid username or password"})

    def test_login_invalid_password(self):
        response = self.fetch("/login", method="PUT", body=json.dumps({
            "username": "Admin",
            "password": "Admin-1234-404"
        }))
        response_data = json.loads(response.body)

        self.assertEqual(response.code, 401)
        self.assertEqual(response_data, {"cause": "Invalid username or password"})

    def test_login_invalid_json(self):
        response = self.fetch("/login", method="PUT", body='{"username":')
        response_data = json.loads(response.body)

        self.assertEqual(response.code, 400)
        self.assertEqual(response_data, {"cause": "Invalid JSON"})
