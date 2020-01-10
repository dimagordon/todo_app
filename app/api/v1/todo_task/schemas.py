from marshmallow import fields

from app.api.common_schemas import TrimmedString
from app.api.common_schemas import UnknownFieldExcludeSchema


class BaseTaskSchema(UnknownFieldExcludeSchema):
    content = TrimmedString(required=True)


class GetTasksSchema(UnknownFieldExcludeSchema):
    todo_list_id = fields.Integer(required=True)


class CreateTaskSchema(BaseTaskSchema, GetTasksSchema):
    pass


class FinishTaskSchema(UnknownFieldExcludeSchema):
    done = fields.Boolean(required=True)


base_task_schema = BaseTaskSchema()
get_tasks_schema = GetTasksSchema()
create_task_schema = CreateTaskSchema()
finish_task_schema = FinishTaskSchema()
