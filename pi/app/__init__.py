from flask import Flask
from app.config import Config
from app.database import db, migrate
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import garden_api
    app.register_blueprint(garden_api)

    return app