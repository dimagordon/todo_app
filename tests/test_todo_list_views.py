import json
from http import HTTPStatus


def test_create_todo_list(client):
    client, app = client

    data = {'title': 'New Todo List'}
    response = client.post(
        '/api/v1/todo-lists',
        data=json.dumps(data),
        content_type='application/json'
    )

    assert response.status_code == HTTPStatus.CREATED


def test_title_unique_constraint(client):
    client, app = client

    data = {'title': 'New Todo List'}
    response = client.post(
        '/api/v1/todo-lists',
        data=json.dumps(data),
        content_type='application/json'
    )

    assert response.status_code == HTTPStatus.CREATED

    data = {'title': 'New Todo List'}
    response = client.post(
        '/api/v1/todo-lists',
        data=json.dumps(data),
        content_type='application/json'
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
