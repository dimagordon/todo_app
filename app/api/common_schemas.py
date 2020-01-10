from marshmallow import fields, Schema, EXCLUDE


class TrimmedString(fields.String):
    def _deserialize(self, value, *args, **kwargs):
        if hasattr(value, 'strip'):
            value = value.strip()
        return super()._deserialize(value, *args, **kwargs)


class UnknownFieldExcludeSchema(Schema):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.unknown = EXCLUDE
