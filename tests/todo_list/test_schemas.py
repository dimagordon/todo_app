from app.api.v1.todo_list.schemas import todo_list_schema


def test_unknonw_field_exclude_schema():
    required_title = {'title': 'some title'}
    unknown_fields_to_exclude = {'foo': 'bar', 'test': 'passed'}
    fields = dict(**required_title, **unknown_fields_to_exclude)
    data = todo_list_schema.load(fields)
