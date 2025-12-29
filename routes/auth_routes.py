from flask import Blueprint, request, jsonify
from services.auth import register_user, login_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    user = register_user(data["email"], data["password"])
    return jsonify({"id": user.id, "email": user.email})


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    token = login_user(data["email"], data["password"])
    return jsonify({"token": token})
