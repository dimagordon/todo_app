from app import db


class TodoLists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False, unique=True)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
        }


class TodoTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False, nullable=False)
    todo_list_id = db.Column(db.Integer, db.ForeignKey('todo_lists.id'), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'content': self.content,
            'done': self.done,
            'todo_list_id': self.todo_list_id
        }
