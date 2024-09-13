import unittest, os
from app import create_app, db
from app.models import Team
from app.services import TeamService

team_service = TeamService()

class TeamTestCase(unittest.TestCase):
    
    def setUp(self):
        # Team
        self.TEAMNAME_TEST = 'Equipo 1'

        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_team(self):  
        team = self.__get_team()

        self.assertIsNotNone(team)
        self.assertEqual(team.team_name, self.TEAMNAME_TEST)

    def test_team_save(self):
        team = self.__get_team()
        team_service.save(team)

        self.assertGreaterEqual(team.id,1)
        self.assertEqual(team.team_name, self.TEAMNAME_TEST)
    
    def test_team_delete(self):
        team = self.__get_team()
        team_service.save(team)

        team_service.delete(team.id)
        self.assertIsNone(team_service.find(team.id))
    
    def test_team_all(self):
        team = self.__get_team()
        team_service.save(team)

        teams = team_service.all()
        self.assertGreaterEqual(len(teams), 1)
    
    def test_team_find(self):
        team = self.__get_team()
        team_service.save(team)

        team_find = team_service.find(1)
        self.assertIsNotNone(team_find)
        self.assertEqual(team_find.id, team.id)
    
    def test_team_find_by_name(self):
        team = self.__get_team()
        team_service.save(team)

        team_find = team_service.find(1)
        self.assertIsNotNone(team_find)
        self.assertEqual(team_find.id, team.id)

    def __get_team(self) -> Team:
        team = Team()
        team.team_name = self.TEAMNAME_TEST

        return team

if __name__ == '__main__':
    unittest.main()