from flask import Flask
from .config import Config
from .extensions import db, jwt
from .routes.health import health_bp
from .routes.booking import booking_bp
from .routes.availability import availability_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(health_bp, url_prefix="/api/health")
    app.register_blueprint(booking_bp, url_prefix="/api/booking")
    app.register_blueprint(availability_bp, url_prefix="/api/availability")

    return app