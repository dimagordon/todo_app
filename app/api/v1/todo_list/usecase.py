from sqlalchemy.exc import IntegrityError, DataError
from marshmallow import ValidationError

from app import db
from app.models import TodoList
from . import errors


class TodoListUseCase:

    todo_list_model = TodoList

    def new_todo_list(self, title):
        todo_list = self.todo_list_model(title=title)
        db.session.add(todo_list)
        try:
            db.session.commit()
        except IntegrityError:
            raise ValidationError(errors.TITLE_DUPLICATE_CONSTRAINT)
        except DataError:
            raise ValidationError(errors.TITLE_LENGTH_CONSTRAINT)
        return todo_list

    def get_all(self):
        return self.todo_list_model.query.all()
