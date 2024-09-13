from app.models import Team
from marshmallow import fields, Schema, post_load

class TeamSchema(Schema):
    id = fields.Integer(dump_only=True)
    team_name = fields.String(required=True)
    
    @post_load
    def make_team(self,data ,**kwargs):
        return Team(**data)
    