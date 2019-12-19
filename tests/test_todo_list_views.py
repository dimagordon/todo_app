import json


def test_create_todo_list(client):
    client, app = client

    data = {'title': 'New Todo List'}
    response = client.post(
        '/v1/todo-lists',
        data=json.dumps(data),
        content_type='application/json'
    )

    assert response.status_code == 201


def test_title_unique_constraint(client):
    client, app = client

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
