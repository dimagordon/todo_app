from http import HTTPStatus
from flask import abort

from flask import (
    Blueprint
)


bp = Blueprint("todo_tasks", __name__, url_prefix="/v1/todo-tasks")


def get_all_tasks():
    pass


def create_task():
    pass


def edit_task():
    pass


def done_task():
    pass


def delete_task():
    pass

