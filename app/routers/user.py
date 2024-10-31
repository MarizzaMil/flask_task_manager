# routers/user.py
from flask import Blueprint, request, jsonify
from app.models.user import db, User
from app.utils.jwt_handler import generate_jwt
from app.utils.validators import validate_email_password
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/auth/signup', methods=['POST'])
def register_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not validate_email_password(email, password):
        return jsonify({"error": "Invalid email or password format"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 409

    new_user = User(email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201


@auth.route('/auth/signin', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = generate_jwt({"user_id": user.id, "email": user.email})

    return jsonify({"token": token, "user": user.to_dict()}), 200
