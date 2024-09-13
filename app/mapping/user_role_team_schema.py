from app.models import UserRoleTeam
from marshmallow import fields, Schema, post_load

class UserRoleTeamSchema(Schema):
    user_id = fields.Integer()
    role_id = fields.Integer()
    team_id = fields.Integer()
    
    @post_load
    def make_user(self, data, **kwargs):
        return UserRoleTeam(**data)
    
    