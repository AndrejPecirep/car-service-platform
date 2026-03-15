from flask import Flask
from flask_cors import CORS

from .config import Config
from .extensions import db, jwt
from .routes.auth import auth_bp
from .routes.availability import availability_bp
from .routes.booking import booking_bp
from .routes.health import health_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    CORS(app)

    app.register_blueprint(health_bp, url_prefix="/api/health")
    app.register_blueprint(booking_bp, url_prefix="/api/booking")
    app.register_blueprint(availability_bp, url_prefix="/api/availability")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    return app
