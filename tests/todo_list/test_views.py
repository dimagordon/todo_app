import json
from http import HTTPStatus

BASE_TODO_POST_LIST_DATA = {'title': 'New Todo List'}


def post_todo_list(client, data):
    response = client.post(
        '/api/v1/todo-lists',
        data=json.dumps(data),
        content_type='application/json'
    )
    return response


def test_create_todo_list(client):
    client, app = client
    response = post_todo_list(client, BASE_TODO_POST_LIST_DATA)
    assert response.status_code == HTTPStatus.CREATED


def test_title_unique_constraint(client):
    client, app = client
    response = post_todo_list(client, BASE_TODO_POST_LIST_DATA)
    assert response.status_code == HTTPStatus.CREATED
    response = post_todo_list(client, BASE_TODO_POST_LIST_DATA)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_trim_title(client):
    client, app = client
    title = '   title   '
    response = post_todo_list(client, {'title': title})
    assert response.status_code == HTTPStatus.CREATED
    assert response.json.get('title') == title.strip()


def test_title_length_constraint(client):
    client, app = client
    title = 'x' * 200
    response = post_todo_list(client, {'title': title})
    assert response.status_code == HTTPStatus.BAD_REQUEST
