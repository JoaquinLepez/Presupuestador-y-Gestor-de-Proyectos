from typing import List

from app.repositories.user_role_team_repository import UserRoleTeamRepository
from app.models import UserRoleTeam, Role, User, Team

class UserRoleTeamService:
    def __init__(self):
        self._repository = UserRoleTeamRepository()

    def all(self) -> List[UserRoleTeam]:
        return self._repository.all()

    # def save(self, urt: UserRoleTeam) -> UserRoleTeam:
    #     return self._repository.save(urt)
    
    # Asignación y remoción de roles
    def add_user_to_team_with_role(self, urt: UserRoleTeam) -> UserRoleTeam:
        return self._repository.add_user_to_team_with_role(urt)
    
    def get_teams_and_roles(self, user_id: int) -> List[UserRoleTeam]:
        return self._repository.get_teams_and_roles(user_id)
    
    def get_users_and_roles(self, team_id: int) -> List[UserRoleTeam]:
        return self._repository.get_users_and_roles(team_id)

    def remove_role_from_user(self, user_id: int, role_id: int, team_id: int) -> bool:
        return self._repository.remove_role_from_user(user_id, role_id, team_id)
    
    # Consultas de roles y usuarios
    def get_user_roles_in_team(self, user_id: int, team_id: int) -> List[Role]:
        return self._repository.get_user_roles_in_team(user_id, team_id)
    
    def get_users_with_role_in_team(self, role_id: int, team_id: int) -> List[User]:
        return self._repository.get_users_with_role_in_team(role_id, team_id)