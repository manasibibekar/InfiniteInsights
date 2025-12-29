import jwt
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app

from extensions import db
from models import User

'''
How JWT flows through the system

POST /login
→ login_user()
→ JWT token returned

Client stores token

Next request:
Authorization: Bearer <token>
→ decode_token()
→ get_current_user()
'''

def register_user(email: str, password: str, is_admin=False) -> User:
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        raise ValueError("User already exists")

    password_hash = generate_password_hash(password)

    user = User(
        email=email,
        password_hash=password_hash,
        is_admin=is_admin
    )

    db.session.add(user)
    db.session.commit()

    return user

def login_user(email: str, password: str) -> str:
    user = User.query.filter_by(email=email).first()
    if not user:
        raise ValueError("Invalid credentials")

    if not check_password_hash(user.password_hash, password):
        raise ValueError("Invalid credentials")

    payload = {
        "sub": user.id,
        "is_admin": user.is_admin,
        "exp": datetime.utcnow() + timedelta(
            seconds=current_app.config["JWT_EXPIRY_SECONDS"]
        )
    }

    token = jwt.encode(
        payload,
        current_app.config["JWT_SECRET_KEY"],
        algorithm=current_app.config["JWT_ALGORITHM"]
    )

    return token

def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(
            token,
            current_app.config["JWT_SECRET_KEY"],
            algorithms=[current_app.config["JWT_ALGORITHM"]]
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")

def get_current_user(token: str) -> User:
    payload = decode_token(token)

    user_id = payload.get("sub")
    user = User.query.get(user_id)

    if not user:
        raise ValueError("User not found")

    return user
