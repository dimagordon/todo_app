from http import HTTPStatus

from flask import request, jsonify
from flask.views import MethodView

from .usecase import TodoListUseCase
from .schemas import todo_list_schema


class TodoListView(MethodView):

    usecase = TodoListUseCase()

    def get(self):
        todo_lists = self.usecase.get_all()
        return jsonify([todo_list.to_json() for todo_list in todo_lists]), HTTPStatus.Ok

    def post(self):
        todo_list_json = todo_list_schema.load(request.json)
        todo_list = self.usecase.new_todo_list(**todo_list_json)
        return jsonify(todo_list.to_json()), HTTPStatus.CREATED


todo_list_api = TodoListView.as_view('todo_list_api')
