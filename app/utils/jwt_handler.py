# utils/jwt_handler.py
import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'your-secret-key'


def generate_jwt(data, expires_in=60):
    payload = {
        "exp": datetime.utcnow() + timedelta(minutes=expires_in),
        "iat": datetime.utcnow(),
        **data
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def decode_jwt(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
