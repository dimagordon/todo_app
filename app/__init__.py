from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import get_config
from app.utils import handle_validation_errors


db = SQLAlchemy()


def create_app(config_prefix):
    app = Flask(__name__)
    app.config.from_object(get_config(config_prefix))

    # Catch all marshmallow ValidationError's and respond with 400 status.
    handle_validation_errors(app)

    db.init_app(app)

    from app.api.v1 import api as api_v1
    app.register_blueprint(api_v1, url_prefix='/api/v1')
    return app


def init_db():
    db.drop_all()
    db.create_all()
