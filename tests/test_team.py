import unittest
from app import create_app, db
from app.models import Team

class TeamTestCase(unittest.TestCase):
    
    def setUp(self):
        # Team
        self.TEAMNAME_PRUEBA = 'Equipo 1'

        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_team(self):
        
        team = self.__get_team()

        # db.session.add(user)
        # db.session.commit()

        self.assertEqual(team.team_name, self.TEAMNAME_PRUEBA)

    def __get_team(self):
        team = Team()
        team.team_name = self.TEAMNAME_PRUEBA

        return team
    

if __name__ == '__main__':
    unittest.main()