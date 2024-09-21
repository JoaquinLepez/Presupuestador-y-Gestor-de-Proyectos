from typing import List
from app.models import UserRoleTeam
from app import db

class UserRoleTeamRepository:

    def all(self) -> List[UserRoleTeam]:
        urt = db.session.query(UserRoleTeam).all()
        return urt

    def add_user_to_team_with_role(self, urt: UserRoleTeam) -> UserRoleTeam:
        db.session.add(urt)
        db.session.commit()
        return urt
    
    def get_teams_and_roles(self, user_id):
        teams = db.session.query(UserRoleTeam.role_id, UserRoleTeam.team_id).filter_by(user_id=user_id).all()
        return teams
    
    def get_users_and_roles(self, team_id):
        result = db.session.query(UserRoleTeam.user_id, UserRoleTeam.role_id).filter_by(team_id=team_id).all()
        print(result)
        return result

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
