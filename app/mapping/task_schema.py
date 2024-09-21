from app.models import Task
from marshmallow import fields, Schema, post_load

class TaskSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=fields.Length(min=1, max=80))
    description = fields.String(required=True, validate=fields.Length(min=1, max=64))
    start_date = fields.DateTime(required=True)
    deadline = fields.DateTime(required=False)
    priority = fields.String(required=True, validate=fields.Length(min=1, max=64))
    difficulty = fields.String(required=True, validate=fields.Length(min=1, max=64))
    state = fields.String(required=True, validate=fields.Length(min=1, max=64))
    # Foreign key
    project_id = fields.Integer(required=True)

    users = fields.List(fields.Nested("UserSchema"), dump_only=True)

    @post_load
    def make_data(self, data, **kwargs):
        return Task(**data)