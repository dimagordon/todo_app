from sqlalchemy.exc import IntegrityError, DataError

from app import db
from app.models import TodoLists


class TodoListUseCase:

    error = None

    def new_todo_list(self, title):
        if not title:
            self.error = {'title': 'Title is required.'}
            return

        todo_list = TodoLists(title=title)
        db.session.add(todo_list)
        try:
            db.session.commit()
        except IntegrityError:
            self.error = {'title': f'Todo list with title "{title}" already exists.'}
        except DataError as e:
            print(e)
            self.error = {'todo-list': 'Something went wrong.'}
