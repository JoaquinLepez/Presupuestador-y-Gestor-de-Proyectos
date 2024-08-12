from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
import os
from app.config import config
from app.routes import RouteApp



db = SQLAlchemy()
migrate = Migrate()
mail = Mail()

def create_app():
    app_context = os.getenv("FLASK_CONTEXT")
    print(f"app_context: {app_context}")

    app = Flask(__name__)
    configuration = config[app_context if app_context else 'development']
    app.config.from_object(configuration)

    route = RouteApp()
    route.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    
    return app
