from app import db
from app.models import TodoTask

from marshmallow import ValidationError

# should be moved to models/errors
from . import errors


class TodoTaskUseCase:

    model = TodoTask

    def get_tasks_by_list_id(self, todo_list_id):
        return self.model.query.filter_by(todo_list_id=todo_list_id)

    def create_task(self, content, todo_list_id):
        task = self.model(content=content, todo_list_id=todo_list_id)
        db.session.add(task)
        db.session.commit()
        return task

    def edit_task(self, task_id, content):
        data_to_update = {'content': content}
        rows = self.model.query.filter_by(id=task_id).update(data_to_update)
        if not rows:
            raise ValidationError(errors.TASK_ID_DOES_NOT_EXIST.format(id_=task_id))
        db.session.commit()
        return data_to_update

    def finish_task(self, task_id):
        rows = self.model.query.filter_by(id=task_id).update({'done': True})
        if not rows:
            raise ValidationError(errors.TASK_ID_DOES_NOT_EXIST.format(id_=task_id))
        db.session.commit()

    def delete_task(self, task_id):
        task = self.model.query.filter_by(id=task_id).first()
        if task is None:
            raise ValidationError(errors.TASK_ID_DOES_NOT_EXIST.format(id_=task_id))
        db.session.delete(task)
        db.session.commit()
