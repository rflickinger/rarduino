from flask import Flask
from app.config import Config
from app.database import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app import models

    db.init_app(app)
    migrate.init_app(app, db)
    
    return app
