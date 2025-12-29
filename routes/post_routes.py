from flask import Blueprint, request, jsonify
from services.post_service import (
    create_post, get_all_posts, get_post,
    update_post, delete_post
)
from utils.auth_guard import jwt_required

post_bp = Blueprint("posts", __name__)

@post_bp.route("/posts", methods=["POST"])
@jwt_required
def create():
    user = request.current_user
    data = request.json

    post = create_post(data["title"], data["content"], user)
    return jsonify({"id": post.id}), 201


@post_bp.route("/posts", methods=["GET"])
def list_posts():
    posts = get_all_posts()
    return jsonify([
        {"id": p.id, "title": p.title, "author_id": p.author_id}
        for p in posts
    ])


@post_bp.route("/posts/<int:post_id>", methods=["PUT"])
@jwt_required
def update(post_id):
    user = request.current_user
    post = get_post(post_id)

    if post.author_id != user.id:
        return jsonify({"error": "Forbidden"}), 403

    data = request.json
    update_post(post, data["title"], data["content"])
    return jsonify({"message": "Updated"})


@post_bp.route("/posts/<int:post_id>", methods=["DELETE"])
@jwt_required
def delete(post_id):
    user = request.current_user
    post = get_post(post_id)

    if post.author_id != user.id and not user.is_admin:
        return jsonify({"error": "Forbidden"}), 403

    delete_post(post)
    return jsonify({"message": "Deleted"})
