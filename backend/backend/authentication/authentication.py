import jwt
import datetime


class Authentication:
    TOKEN_EXPIRATION_TIME = datetime.timedelta(hours=1)
    JWT_SECRET = "random-secret"
    JWT_ALGORITHM = "HS256"

    def now(self):
        return datetime.datetime.now(tz=datetime.timezone.utc)

    def generate_expiration_datetime(self):
        return (self.now() + self.TOKEN_EXPIRATION_TIME).isoformat()

    def generate_token(self, payload):
        payload["exp"] = self.generate_expiration_datetime()
        return jwt.encode(payload, self.JWT_SECRET, algorithm=self.JWT_ALGORITHM)
