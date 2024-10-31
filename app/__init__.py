# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from app.config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # Enable CORS for all routes
    CORS(app)

    # Load configuration from the Config class
    app.config.from_object(Config)

    # Initialize database and migration utilities
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register blueprints
    from app.routers import task
    app.register_blueprint(task.bp)

    # You can register additional blueprints here as needed

    return app
