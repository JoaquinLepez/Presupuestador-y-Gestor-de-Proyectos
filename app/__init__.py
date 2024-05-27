from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config
from .resources import main as main_blueprint

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)

    app.register_blueprint(main_blueprint)

    return app