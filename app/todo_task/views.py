from http import HTTPStatus

from flask import (
    Blueprint, request, make_response, jsonify, abort
)

from .usecase import TodoTaskUseCase


bp = Blueprint("todo_tasks", __name__, url_prefix="/v1/todo-tasks")


@bp.route('', methods=('GET',))
def get_all_tasks_by_todo_list_id():
    if not request.is_json:
        return abort(HTTPStatus.BAD_REQUEST)

    usecase = TodoTaskUseCase()
    tasks = usecase.get_todo_list_tasks(todo_list_id=request.args.get('todo_list_id'))
    if usecase.error:
        return jsonify({"error": usecase.error}), HTTPStatus.BAD_REQUEST
    return jsonify(tasks), HTTPStatus.OK


@bp.route('', methods=('POST',))
def create_task():
    if not request.is_json:
        return abort(HTTPStatus.BAD_REQUEST)

    usecase = TodoTaskUseCase()
    task = usecase.create_task(
        content=request.json.get('content'),
        todo_list_id=request.json.get('todo_list_id')
    )
    if usecase.error:
        return jsonify({"error": usecase.error}), HTTPStatus.BAD_REQUEST
    return jsonify(task.to_json()), HTTPStatus.CREATED


def edit_task():
    pass


@bp.route('<int:task_id>/finish', methods=('PATCH',))
def finish_task(task_id):
    if not request.is_json:
        return abort(HTTPStatus.BAD_REQUEST)

    usecase = TodoTaskUseCase()
    usecase.finish_task(task_id=task_id)
    if usecase.error:
        return jsonify({"error": usecase.error}), HTTPStatus.BAD_REQUEST
    return make_response(), HTTPStatus.OK


@bp.route('<int:task_id>', methods=('DELETE',))
def delete_task(task_id):
    usecase = TodoTaskUseCase()
    usecase.delete_task(task_id=task_id)
    if usecase.error:
        return jsonify({"error": usecase.error}), HTTPStatus.BAD_REQUEST
    return make_response(), HTTPStatus.NO_CONTENT
