# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    CORS(app)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routers import task
    app.register_blueprint(task.bp)
    from app.routers.user import auth
    app.register_blueprint(auth)

    return app
