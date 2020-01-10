from app import db


TODO_LIST_TITLE_LENGTH_CONSTRAINT = 60


class TodoList(db.Model):
    __tablename__ = 'todo_lists'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(TODO_LIST_TITLE_LENGTH_CONSTRAINT), nullable=False, unique=True)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
        }


class TodoTask(db.Model):
    __tablename__ = 'todo_tasks'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    done = db.Column(db.Boolean, default=False, nullable=False)
    todo_list_id = db.Column(db.Integer, db.ForeignKey('todo_lists.id'), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'content': self.content,
            'done': self.done,
            'todo_list_id': self.todo_list_id
        }
