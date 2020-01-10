from marshmallow import validate

from app.api.common_schemas import TrimmedString
from app.api.common_schemas import UnknownFieldExcludeSchema
from app.models import TODO_LIST_TITLE_LENGTH_CONSTRAINT


class TodoListSchema(UnknownFieldExcludeSchema):
    title = TrimmedString(
        required=True,
        validate=validate.Length(max=TODO_LIST_TITLE_LENGTH_CONSTRAINT))


todo_list_schema = TodoListSchema()
