import json
from http import HTTPStatus

import pytest

from app import create_app, init_db
from app.todo_list.usecase import TodoListUseCase
from app.todo_task.usecase import TodoTaskUseCase


@pytest.fixture
def client():
    app = create_app('test')
    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client, app


def test_create_todo_task(client):
    client, app = client
    with app.app_context():
        uc = TodoListUseCase()
        todo_list = uc.new_todo_list('new')
        id_ = todo_list.id
    data = {'content': 'New Todo task', 'todo_list_id': id_}
    response = client.post(
        '/v1/todo-tasks',
        data=json.dumps(data),
        content_type='application/json'
    )

    assert response.status_code == 201


def test_delete_todo_task(client):
    client, app = client
    with app.app_context():
        todo_list_usecase = TodoListUseCase()
        todo_list = todo_list_usecase.new_todo_list('new')

        todo_task_usecase = TodoTaskUseCase()
        todo_task = todo_task_usecase.create_task("some content", todo_list.id)

    response = client.delete(
        f'/v1/todo-tasks/{todo_task.id}',
    )
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_delete_todo_task_fail(client):
    client, app = client
    response = client.delete(
        f'/v1/todo-tasks/{200}',
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert 'error' in response.json


def test_finish_todo_task(client):
    client, app = client
    with app.app_context():
        todo_list_usecase = TodoListUseCase()
        todo_list = todo_list_usecase.new_todo_list('new')

        todo_task_usecase = TodoTaskUseCase()
        todo_task = todo_task_usecase.create_task("some content", todo_list.id)
        assert not todo_task.done

    response = client.patch(
        f'/v1/todo-tasks/{todo_task.id}/finish',
        content_type='application/json'
    )
    assert response.status_code == HTTPStatus.OK