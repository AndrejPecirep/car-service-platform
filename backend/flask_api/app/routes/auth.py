from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.extensions import db
from sqlalchemy import text
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    if "email" not in data or "password" not in data:
        return jsonify({"error": "Email and password required"}), 400

    query = text("SELECT id, email, password FROM users_user WHERE email = :email")
    user = db.session.execute(query, {"email": data["email"]}).fetchone()
    if not user or not check_password_hash(user.password, data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=user.id)
    return jsonify(access_token=token, user_id=user.id, email=user.email)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    required_fields = ["email", "first_name", "last_name", "password"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    existing_user = db.session.execute(text("SELECT id FROM users_user WHERE email = :email"), {"email": data["email"]}).fetchone()
    if existing_user:
        return jsonify({"error": "User already exists"}), 400

    hashed_password = generate_password_hash(data["password"])
    try:
        result = db.session.execute(text("""
            INSERT INTO users_user (email, first_name, last_name, password, is_active)
            VALUES (:email, :first_name, :last_name, :password, TRUE)
            RETURNING id
        """), {
            "email": data["email"],
            "first_name": data["first_name"],
            "last_name": data["last_name"],
            "password": hashed_password
        })
        db.session.commit()
        user_id = result.fetchone()[0]
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    token = create_access_token(identity=user_id)
    return jsonify(access_token=token, user_id=user_id, email=data["email"])