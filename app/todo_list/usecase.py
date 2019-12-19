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
            # for now I don't know why. But a can't get todo_list->id property outside this try context
            # so save id here
            todo_list_id = todo_list.id
        except IntegrityError:
            self.error = {'title': f'Todo list with title "{title}" already exists.'}
        except DataError as e:
            logger.exception(e)
            self.error = {'todo-list': 'Something went wrong.'}
        else:
            return TodoList.query.get(todo_list_id)
