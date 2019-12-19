from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import get_config


db = SQLAlchemy()


def create_app(config_prefix):
    app = Flask(__name__)
    app.config.from_object(get_config(config_prefix))

    db.init_app(app)

    from app.todo_list.views import bp as todo_list_bp
    from app.todo_task.views import bp as todo_task_bp
    app.register_blueprint(todo_list_bp)
    app.register_blueprint(todo_task_bp)

    return app


def init_db():
    db.drop_all()
    db.create_all()
