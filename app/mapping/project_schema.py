from app.models import Project
from marshmallow import fields, Schema, post_load

class ProjectSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=fields.Length(min=1, max=30))
    description = fields.String(required=True, validate=fields.Length(min=1, max=250))
    start_date = fields.DateTime(required=True)
    deadline = fields.DateTime(required=False)
    state = fields.String(required=True, validate=fields.Length(min=1, max=120))

    @post_load
    def make_data(self, data, **kwargs):
        return Project(**data)