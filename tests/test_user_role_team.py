import unittest,os
from typing import List
from app import create_app, db
from app.models import User, Role, Team, UserRoleTeam
from app.services import UserService, RoleService, TeamService

user_service = UserService()
role_service = RoleService()
team_service = TeamService()

class UserRoleTeamTestCase(unittest.TestCase):
    
    def setUp(self):
        # Users
        self.USERNAME_TEST1 = 'ramandu'
        self.PASSWORD_TEST1 = '123456'
        self.EMAIL_TEST1 = 'test@test.com'

        self.USERNAME_TEST2 = 'gandalf'
        self.PASSWORD_TEST2 = '456789'
        self.EMAIL_TEST2 = 'test2@test2.com'

        # Team
        self.TEAMNAME_TEST1 = 'Equipo 1'
        self.TEAMNAME_TEST2 = 'Equipo 2'

        # Role
        self.ROLENAME_TEST = 'Admin'
    
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_UserRoleTeam(self):
        user = self.__get_users()[0]
        role = self.__get_role()
        team = self.__get_teams()[0]

        user_service.save(user)
        role_service.save(role)
        team_service.save(team)

        user_role_team = UserRoleTeam(user_id= user.id, role_id = role.id, team_id = team.id)
        db.session.add(user_role_team)
        db.session.commit()

        self.assertIsNotNone(user_role_team)
        self.assertEqual(user_role_team.user.username, self.USERNAME_TEST1)
        self.assertEqual(user_role_team.role.name, self.ROLENAME_TEST)
        self.assertEqual(user_role_team.team.team_name, self.TEAMNAME_TEST1)

    def test_user(self):
        user1 = self.__get_users()[0]
        team1 = self.__get_teams()[0]
        team2 = self.__get_teams()[1]
        role = self.__get_role()

        user_service.save(user1)
        role_service.save(role)
        team_service.save(team1)
        team_service.save(team2)

        urt1 = UserRoleTeam(user_id= user1.id, role_id = role.id, team_id = team1.id)
        urt2 = UserRoleTeam(user_id= user1.id, role_id = role.id, team_id = team2.id)
        db.session.add(urt1)
        db.session.add(urt2)
        db.session.commit()

        self.assertEqual(user1.teams_roles[0].team.team_name, self.TEAMNAME_TEST1)
        self.assertEqual(user1.teams_roles[1].team.team_name, self.TEAMNAME_TEST2)

    def __get_users(self) -> List[User]:
        user1 = User()
        user1.username = self.USERNAME_TEST1
        user1.email = self.EMAIL_TEST1
        user1.password = self.PASSWORD_TEST1

        user2 = User()
        user2.username = self.USERNAME_TEST2
        user2.email = self.EMAIL_TEST2
        user2.password = self.PASSWORD_TEST2

        return [user1, user2]
    
    def __get_role(self) -> Role:
        role = Role()
        role.name = self.ROLENAME_TEST

        return role
    
    def __get_teams(self) -> List[Team]:
        team1 = Team()
        team1.team_name = self.TEAMNAME_TEST1

        team2 = Team()
        team2.team_name = self.TEAMNAME_TEST2

        return [team1, team2]
    

if __name__ == '__main__':
    unittest.main()