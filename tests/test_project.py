import unittest
from app import create_app, db
from app.models import Project

class ProjectTestCase(unittest.TestCase):
    
    def setUp(self):
        # Project
        self.NAME_PRUEBA = 'Proyecto Ultra'
        self.DESCRIPTION_PRUEBA = 'Do Not Develop My App'
        self.STARTDATE_PRUEBA = '9/12/18'
        self.DEADLINE_PRUEBA = '9/7/24'
        self.STATE_PRUEBA = 'In Progress'

        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_project(self):
        
        project = self.__get_project()

        # db.session.add(user)
        # db.session.commit()

        self.assertEqual(project.name, self.NAME_PRUEBA)
        self.assertEqual(project.description, self.DESCRIPTION_PRUEBA)
        self.assertEqual(project.start_date, self.STARTDATE_PRUEBA)
        self.assertEqual(project.deadline, self.DEADLINE_PRUEBA)
        self.assertEqual(project.state, self.STATE_PRUEBA)

    def __get_project(self):
        team = Project()
        team.name = self.NAME_PRUEBA
        team.description = self.DESCRIPTION_PRUEBA
        team.start_date = self.STARTDATE_PRUEBA
        team.deadline = self.DEADLINE_PRUEBA
        team.state = self.STATE_PRUEBA

        return team
    

if __name__ == '__main__':
    unittest.main()