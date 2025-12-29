from functools import wraps
from flask import request, jsonify
from utils.jwt_utils import decode_token
from models.user import User

def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing token"}), 401

        token = auth_header.split(" ")[1]

        try:
            payload = decode_token(token)
            user = User.query.get(payload["sub"])

            if not user:
                return jsonify({"error": "User not found"}), 401

            request.current_user = user

        except Exception:
            return jsonify({"error": "Invalid or expired token"}), 401

        return fn(*args, **kwargs)

    return wrapper
