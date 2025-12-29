from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from extensions import db
from utils.jwt_utils import create_token

def register_user(email, password):
    if User.query.filter_by(email=email).first():
        raise ValueError("User already exists")

    user = User(
        email=email,
        password_hash=generate_password_hash(password)
    )

    db.session.add(user)
    db.session.commit()
    return user


def login_user(email, password):
    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password_hash, password):
        raise ValueError("Invalid credentials")

    return create_token(user.id, user.is_admin)
