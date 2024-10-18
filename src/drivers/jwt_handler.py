import jwt
from datetime import timedelta, datetime, timezone
from src.configs.jwt_configs import jwt_infos

class JwtHandler:
    def create_jwt_token(self, body: dict = {}) -> str:
        token = jwt.encode(
            payload={
                'exp': datetime.now(timezone.utc) + timedelta(hours=int(jwt_infos['JWT_HOURS'])),
                **body
            },
            key=jwt_infos['KEY'],
            algorithm=jwt_infos['ALGORITHM']
        )

        return token

    def decode_jwt_token(self, token: str) -> dict:
        token_information = jwt.decode(
            jwt=token,
            key="minhaChave",
            algorithms="HS256"
        )
        return token_information
