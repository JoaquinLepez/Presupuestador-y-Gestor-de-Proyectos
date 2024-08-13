from app.models.user_role_team import UserRoleTeam
from app import db

class UserRoleTeamRepository:

    def assign_role_to_user(self, user_id, role_id, team_id):
        user_role_team = UserRoleTeam(user_id=user_id, role_id=role_id, team_id=team_id)
        db.session.add(user_role_team)
        db.session.commit()
        return user_role_team
    
    def remove_role_from_user(self, user_id, role_id, team_id):
        user_role_team = db.session.query(UserRoleTeam).filter_by(user_id=user_id, role_id=role_id, team_id=team_id).one_or_none()
        if user_role_team:
            db.session.delete(user_role_team)
            db.session.commit()
            return True
        return False
    
    def get_user_roles_in_team(self, user_id, team_id):
        return db.session.query(UserRoleTeam).filter_by(user_id=user_id, team_id=team_id).all()
    
    def get_users_with_role_in_team(self, role_id, team_id):
        return db.session.query(UserRoleTeam).filter_by(role_id=role_id, team_id=team_id).all()
