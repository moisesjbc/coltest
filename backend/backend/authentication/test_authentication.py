import jwt
import unittest
from unittest.mock import MagicMock, Mock
import datetime
from .authentication import Authentication


class TestAuthentication(unittest.TestCase):
    def test_generate_expiration_datetime(self):
        auth = Authentication()
        auth.now = Mock(return_value=datetime.datetime(2022, 5, 1, 13, 45, tzinfo=datetime.timezone.utc))
        expected_datetime = "2022-05-01T14:45:00+00:00"

        self.assertEqual(auth.generate_expiration_datetime(), expected_datetime)

    def test_generate_token(self):
        expiration_datetime = "2022-05-01T14:45:00"
        auth = Authentication()
        auth.generate_expiration_datetime = MagicMock(return_value=expiration_datetime)

        expected_token = "expected_token"
        jwt.encode = MagicMock(return_value=expected_token)

        payload = {
            "foo": "bar"
        }
        self.assertEqual(auth.generate_token(payload), expected_token)

        jwt.encode.assert_called_with({
            "foo": "bar",
            "exp": expiration_datetime
        }, Authentication.JWT_SECRET, algorithm=Authentication.JWT_ALGORITHM)


if __name__ == '__main__':
    unittest.main()
