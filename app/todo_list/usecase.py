from sqlalchemy.exc import IntegrityError, DataError

from app import db
from app.models import TodoList
from app.utils import logger


class TodoListUseCase:

    error = None

    def new_todo_list(self, title):
        if not title:
            self.error = {'title': 'Title is required.'}
            return

        todo_list = TodoList(title=title)
        db.session.add(todo_list)
        try:
            db.session.commit()
        except IntegrityError:
            self.error = {'title': f'Todo list with title "{title}" already exists.'}
        except DataError as e:
            logger.exception(e)
            self.error = {'todo-list': 'Something went wrong.'}
        else:
            return todo_list
