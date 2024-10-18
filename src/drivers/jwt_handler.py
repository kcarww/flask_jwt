import jwt
from datetime import timedelta, datetime, timezone


class JwtHandler:
    def create_jwt_token(self, body: dict = {}) -> str:
        token = jwt.encode(
            payload={
                'exp': datetime.now(timezone.utc) + timedelta(minutes=1),
                **body
            },
            key="minhaChave",
            algorithm="HS256"
        )

        return token

    def decode_jwt_token(self, token: str) -> dict:
        token_information = jwt.decode(
            jwt=token,
            key="minhaChave",
            algorithms="HS256"
        )
        return token_information
