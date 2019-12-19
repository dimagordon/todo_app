from app import db
from app.models import TodoLists


class TodoListUseCase:

    error = None

    def new_todo_list(self, title):
        if not title:
            self.error = {"title": "Title is required."}
            return

        todo_list = TodoLists(title=title)
        db.session.add(todo_list)
        db.commit()
