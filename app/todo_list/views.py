from http import HTTPStatus

from flask import (
    Blueprint, request, jsonify
)

from app.todo_list.usecase import TodoListUseCase
from app.utils import is_json_request


bp = Blueprint("todo_lists", __name__, url_prefix="/v1/todo-lists")


@bp.route("", methods=["POST"])
@is_json_request
def new_todo_list():
    usecase = TodoListUseCase()
    todo_list = usecase.new_todo_list(request.json.get('title'))
    if usecase.error:
        return jsonify({"error": usecase.error}), HTTPStatus.BAD_REQUEST
    return jsonify(todo_list.to_json()), HTTPStatus.CREATED
