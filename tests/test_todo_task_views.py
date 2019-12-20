import json
from http import HTTPStatus

from app.todo_list.usecase import TodoListUseCase
from app.todo_task.usecase import TodoTaskUseCase


def test_create_todo_task(client):
    client, app = client
    with app.app_context():
        uc = TodoListUseCase()
        todo_list = uc.new_todo_list('new')
        id_ = todo_list.id
    data = {'content': 'New Todo task', 'todo_list_id': id_}
    response = client.post(
        '/api/v1/todo-tasks',
        data=json.dumps(data),
        content_type='application/json'
    )

    assert response.status_code == HTTPStatus.CREATED


def test_delete_todo_task(client):
    client, app = client
    with app.test_request_context():
        todo_list_usecase = TodoListUseCase()
        todo_list = todo_list_usecase.new_todo_list('new')

        todo_task_usecase = TodoTaskUseCase()
        todo_task = todo_task_usecase.create_task("some content", todo_list.id)
        todo_task_id = todo_task.id

    response = client.delete(
        f'/api/v1/todo-tasks/{todo_task_id}',
    )
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_delete_todo_task_fail(client):
    client, app = client
    response = client.delete(
        f'/api/v1/todo-tasks/{200}',
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert 'error' in response.json


def test_edit_todo_task(client):
    client, app = client
    with app.test_request_context():
        todo_list_usecase = TodoListUseCase()
        todo_list = todo_list_usecase.new_todo_list('new')

        todo_task_usecase = TodoTaskUseCase()
        todo_task = todo_task_usecase.create_task("some content", todo_list.id)
        todo_task_id = todo_task.id

    new_content = 'new_content'
    response = client.patch(
        f'/api/v1/todo-tasks/{todo_task_id}/edit',
        data=json.dumps({'content': new_content}),
        content_type='application/json',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json.get('content') == new_content


def test_finish_todo_task(client):
    client, app = client
    with app.app_context():
        todo_list_usecase = TodoListUseCase()
        todo_list = todo_list_usecase.new_todo_list('new')

        todo_task_usecase = TodoTaskUseCase()
        todo_task = todo_task_usecase.create_task("some content", todo_list.id)
        todo_task_id = todo_task.id

    response = client.patch(
        f'/api/v1/todo-tasks/{todo_task_id}/finish',
        content_type='application/json'
    )
    assert response.status_code == HTTPStatus.OK


def test_get_all_tasks(client):
    client, app = client

    with app.app_context():
        todo_list_usecase = TodoListUseCase()
        todo_list = todo_list_usecase.new_todo_list('new')

        todo_list_id = todo_list.id
        todo_task_usecase = TodoTaskUseCase()
        todo_task = todo_task_usecase.create_task("some content", todo_list_id)
        todo_task_id = todo_task.id

    response = client.get(
        f'/api/v1/todo-tasks?todo_list_id={todo_list_id}',
        content_type='application/json'
    )
    assert response.status_code == HTTPStatus.OK
    data = response.json
    assert len(data) == 1
    assert set(data[0].keys()) == {'content', 'done', 'id', 'todo_list_id'}
    assert todo_task_id == data[0].get('id')
    assert todo_list_id == data[0].get('todo_list_id')
