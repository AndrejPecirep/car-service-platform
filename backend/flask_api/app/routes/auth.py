from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.extensions import db
from sqlalchemy import text

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    query = text("""
        SELECT id, email
        FROM users_user
        WHERE email = :email
    """)

    user = db.session.execute(query, {
        "email": data["email"]
    }).fetchone()

    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=user.id)

    return jsonify(
        access_token=token,
        user_id=user.id,
        email=user.email
    )