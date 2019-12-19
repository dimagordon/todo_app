from app.models import TodoTask
from app import db


class TaskUseCase:

    error = None

    def create_task(self, content, todo_list_id):
        if not content or not todo_list_id:
            self.error = "Bad Params"
            return

        task = TodoTask(content=content, todo_list_id=todo_list_id)
        db.session.add(task)
        db.commit()

    def edit_task(self):
        pass

    def finish_task(self, task_id):
        rows = TodoTask.query.filter_by(id=task_id).update({'done': True})
        db.session.commit()
        if not rows:
            self.error = f'Task with id {task_id} does not exist.'
            return

    def delete_task(self, task_id):
        task = TodoTask.query.filter_by(id=task_id).first()
        if task is None:
            self.error = f'Task with id {task_id} does not exist.'
            return
        db.session.delete(task)
        db.session.commit()
