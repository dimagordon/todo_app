import pytest

from app import create_app, init_db


@pytest.fixture
def client():
    app = create_app('test')
    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client, app
