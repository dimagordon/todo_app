from http import HTTPStatus
from flask import abort

from flask import (
    Blueprint, request, make_response, jsonify
)

from app.todo_list.usecase import TodoListUseCase


bp = Blueprint("todo_lists", __name__, url_prefix="/v1/todo-lists")


@bp.route("/", methods=["POST"])
def new_todo_list():
    if not request.is_json():
        return abort(HTTPStatus.BAD_REQUEST)

    usecase = TodoListUseCase()
    usecase.new_todo_list(request.json.get('title'))
    if usecase.error:
        return jsonify({"error": usecase.error}), HTTPStatus.BAD_REQUEST
    return make_response(), HTTPStatus.CREATED
