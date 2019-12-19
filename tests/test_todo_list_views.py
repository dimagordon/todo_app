import json

import pytest


from app import create_app, init_db


@pytest.fixture
def client():
    app = create_app('test')
    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client


def test_create_todo_list(client):
    data = {'title': 'New Todo List'}
    response = client.post(
        '/v1/todo-lists',
        data=json.dumps(data),
        content_type='application/json'
    )

    assert response.status_code == 201


def test_title_unique_constraint(client):
    data = {'title': 'New Todo List'}
    response = client.post(
        '/v1/todo-lists',
        data=json.dumps(data),
        content_type='application/json'
    )

    assert response.status_code == 201

    data = {'title': 'New Todo List'}
    response = client.post(
        '/v1/todo-lists',
        data=json.dumps(data),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.is_json
