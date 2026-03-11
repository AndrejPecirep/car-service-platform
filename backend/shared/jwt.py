import jwt
import os
from datetime import datetime, timedelta

SECRET = os.getenv("JWT_SECRET_KEY")


def create_token(user_id):
    payload = {
        "sub": user_id,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }

    return jwt.encode(payload, SECRET, algorithm="HS256")


def verify_token(token):
    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None