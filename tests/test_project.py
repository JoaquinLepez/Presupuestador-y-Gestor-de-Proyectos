import unittest, os
from app import create_app, db
from app.models import Project
from app.services import ProjectService
from datetime import datetime

project_service = ProjectService()

class ProjectTasteCase(unittest.TestCase):

    def setUp(self):   
        # Project
        self.NAME_TEST = "mi proyecto"
        self.DESCRIPTION_TEST = "esta es la descripcion de mi proyecto"
        self.START_DATE_TEST = datetime(2024,1,1,0,0,0)
        self.DEADLINE_TEST = datetime(2024,2,28,16,34,33)
        self.STATE_TEST = "en proceso"

        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_project(self):
        project = self.__get_project()

        self.assertEqual(project.name, self.NAME_TEST)
        self.assertEqual(project.description, self.DESCRIPTION_TEST)
        self.assertEqual(project.start_date, self.START_DATE_TEST)
        self.assertEqual(project.deadline, self.DEADLINE_TEST)
        self.assertEqual(project.state, self.STATE_TEST)
    
    def test_project_save(self):
        project = self.__get_project()

        project_service.save(project)

        self.assertGreaterEqual(project.id,1)
        self.assertEqual(project.name, self.NAME_TEST)
        self.assertEqual(project.description, self.DESCRIPTION_TEST)
        self.assertEqual(project.start_date, self.START_DATE_TEST)
        self.assertEqual(project.deadline, self.DEADLINE_TEST)
        self.assertEqual(project.state, self.STATE_TEST)
    
    def test_project_delete(self):
        project = self.__get_project()
        project_service.save(project)

        project_service.delete(project.id)
        self.assertIsNone(project_service.find(project.id))

    def test_project_all(self):
        project = self.__get_project()
        project_service.save(project)

        projects = project_service.all()
        self.assertGreaterEqual(len(projects), 1) 
    
    def test_project_find(self):
        project = self.__get_project()
        project_service.save(project)

        project_find = project_service.find(1)
        self.assertIsNotNone(project_find)
        self.assertEqual(project_find.id, project.id)
    
    def test_project_find_by_name(self):
        project = self.__get_project()
        project_service.save(project)

        project_find = project_service.find_by_name(project.name)
        self.assertIsNotNone(project_find)
        self.assertEqual(project_find.id, project.id)

    def __get_project(self) -> Project:
        project = Project()
        project.name = self.NAME_TEST
        project.description = self.DESCRIPTION_TEST
        project.start_date = self.START_DATE_TEST
        project.deadline = self.DEADLINE_TEST
        project.state = self.STATE_TEST

        return project
    

if __name__ == '__main__':
    unittest.main()