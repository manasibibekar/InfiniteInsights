import jwt
import time
from flask import current_app

def create_token(user_id, is_admin=False):
    payload = {
        "sub": user_id,
        "is_admin": is_admin,
        "exp": int(time.time()) + current_app.config["JWT_EXPIRY_SECONDS"]
    }

    return jwt.encode(
        payload,
        current_app.config["JWT_SECRET_KEY"],
        algorithm=current_app.config["JWT_ALGORITHM"]
    )


def decode_token(token):
    return jwt.decode(
        token,
        current_app.config["JWT_SECRET_KEY"],
        algorithms=[current_app.config["JWT_ALGORITHM"]]
    )
