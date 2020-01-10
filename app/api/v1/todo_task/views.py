from http import HTTPStatus

from flask import request, make_response, jsonify
from flask.views import MethodView

from .usecase import TodoTaskUseCase
from . import schemas


class TodoTaskApi(MethodView):

    usecase = TodoTaskUseCase()

    def get(self):
        data = schemas.get_tasks_schema.load(request.args)
        tasks = self.usecase.get_tasks_by_list_id(**data)
        return jsonify([task.to_json() for task in tasks]), HTTPStatus.OK

    def post(self):
        data = schemas.create_task_schema.load(request.json)
        task = self.usecase.create_task(**data)
        return jsonify(task.to_json()), HTTPStatus.CREATED

    def patch(self, task_id):
        data = schemas.base_task_schema.load(request.json)
        updated_data = self.usecase.edit_task(task_id, **data)
        return jsonify(updated_data), HTTPStatus.OK

    def delete(self, task_id):
        self.usecase.delete_task(task_id=task_id)
        return make_response(), HTTPStatus.NO_CONTENT


def finish_task(task_id):
    usecase = TodoTaskUseCase()
    usecase.finish_task(task_id=task_id)
    return make_response(), HTTPStatus.OK


todo_task_api = TodoTaskApi.as_view('todo_task_api')
