import logging
from flask import Blueprint, request, jsonify
from app.models.user import db, User
from app.utils.jwt_handler import generate_jwt
from app.utils.validators import validate_email_password

auth = Blueprint('auth', __name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Route Documentation: User Registration and Authentication


@auth.route('/auth/signup', methods=['POST'])
def register_user():
    """
    Register a new user.

    Expected request JSON:
        - email: string, required, user email
        - password: string, required, user password

    Returns:
        - 201: User created successfully with user details.
        - 400: Invalid email or password format.
        - 409: User already exists.
    """
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not validate_email_password(email, password):
            logger.warning("Invalid email or password format")
            return jsonify({"error": "Invalid email or password format"}), 400

        if User.query.filter_by(email=email).first():
            logger.info("User with email %s already exists", email)
            return jsonify({"error": "User already exists"}), 409

        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        logger.info("New user registered with email: %s", email)

        token = generate_jwt({"user_id": new_user.id, "email": new_user.email})
        logger.info("User %s logged in successfully", email)

        return jsonify({"token": token, "user": new_user.to_dict()}), 201

    except Exception as e:
        logger.error("Error in registering user: %s", e)
        db.session.rollback()
        return jsonify({"error": "An error occurred while creating the user"}), 500


@auth.route('/auth/signin', methods=['POST'])
def login_user():
    """
    Authenticate a user and generate a JWT.

    Expected request JSON:
        - email: string, required, user email
        - password: string, required, user password

    Returns:
        - 200: Login successful with JWT and user details.
        - 401: Invalid credentials.
    """
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()

        if not user or not user.check_password(password):
            logger.warning("Failed login attempt for email: %s", email)
            return jsonify({"error": "Invalid credentials"}), 401

        token = generate_jwt({"user_id": user.id, "email": user.email})
        logger.info("User %s logged in successfully", email)

        return jsonify({"token": token, "user": user.to_dict()}), 200

    except Exception as e:
        logger.error("Error in user login: %s", e)
        return jsonify({"error": "An error occurred while logging in"}), 500
