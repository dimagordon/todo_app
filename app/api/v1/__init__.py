from flask import Blueprint

from .todo_list.views import todo_list_api
from .todo_task.views import todo_task_api, TodoTaskApi, finish_task


def create_api():
    api = Blueprint('api_v1', __name__)
    api.add_url_rule('/todo-lists', view_func=todo_list_api, methods=['GET', 'POST'])
    api.add_url_rule('/todo-tasks', view_func=todo_task_api, methods=['GET', 'POST'])
    api.add_url_rule('/todo-tasks/<int:task_id>', view_func=todo_task_api, methods=['PATCH', 'DELETE'])
    api.add_url_rule('/todo-tasks/<int:task_id>', view_func=todo_task_api, methods=['DELETE'])
    api.add_url_rule('/todo-tasks/<int:task_id>/finish', view_func=finish_task, methods=['PATCH'])
    return api


api = create_api()
