import os
import logging
from functools import wraps
from http import HTTPStatus

from flask import abort, request

logger = logging.getLogger('TodoListLogger')
logger.setLevel(os.environ.get('LOGGER_LEVEL', logging.WARNING))


def is_json_request(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.is_json:
            abort(HTTPStatus.BAD_REQUEST)
        return f(*args, **kwargs)
    return decorated_function
