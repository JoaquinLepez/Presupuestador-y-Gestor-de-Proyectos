import unittest, os
from app import create_app, db
from app.models import Project, Task
from app.services import ProjectService

project_service = ProjectService()

class ProjectTasteCase(unittest.TestCase):

    def setUp(self):   
        # Project
        self.NAME_TEST = "mi proyecto"
        self.DESCRIPTION_TEST = "esta es la descripcion de mi proyecto"
        self.START_DATE_TEST = "1/1/2024"
        self.DEADLINE_TEST = "28/2/2024"
        self.STATE_TEST = "en proceso"
        # Task 1
        self.TASK1_NAME_TEST = "TEST número 1"
        self.TASK1_DESCRIPTION_TEST = "esta es la descripcion de mi TEST número 1"
        self.TASK1_START_DATE_TEST = "1/1/2024"
        self.TASK1_DEADLINE_TEST = "28/2/2024"
        self.TASK1_PRIORITY_TEST = "alta prioridad"
        self.TASK1_DIFFICULTY_TEST = "elevada"
        self.TASK1_STATE_TEST = "en proceso"

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

        self.assertTrue(project.name, self.NAME_TEST)
        self.assertTrue(project.description, self.DESCRIPTION_TEST)
        self.assertTrue(project.start_date, self.START_DATE_TEST)
        self.assertTrue(project.deadline, self.DEADLINE_TEST)
        self.assertTrue(project.state, self.STATE_TEST)
        self.assertIsNotNone(project.task[0])
        self.assertEqual(project.task[0].name, self.TASK1_NAME_TEST)
    
    def test_project_save(self):
        project = self.__get_project()

        project_service.save(project)

        self.assertGreaterEqual(project.id,1)
        self.assertEqual(project.name, self.NAME_TEST)
        self.assertEqual(project.description, self.DESCRIPTION_TEST)
        self.assertEqual(project.start_date, self.START_DATE_TEST)
        self.assertEqual(project.deadline, self.DEADLINE_TEST)
        self.assertEqual(project.state, self.STATE_TEST)
        self.assertIsNotNone(project.task[0])
        self.assertEqual(project.task[0].name, self.TASK1_NAME_TEST)
    
    def test_project_delete(self):
        project = self.__get_project()
        project_service.save(project)

        project_service.delete(project)
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

        task1 = Task()
        task1.name = self.TASK1_NAME_TEST
        task1.description = self.TASK1_DESCRIPTION_TEST
        task1.start_date = self.TASK1_START_DATE_TEST
        task1.deadline = self.TASK1_DEADLINE_TEST
        task1.priority = self.TASK1_PRIORITY_TEST
        task1.difficulty = self.TASK1_DIFFICULTY_TEST
        task1.state = self.TASK1_STATE_TEST

        project = Project()
        project.name = self.NAME_TEST
        project.description = self.DESCRIPTION_TEST
        project.start_date = self.START_DATE_TEST
        project.deadline = self.DEADLINE_TEST
        project.state = self.STATE_TEST

        project.task.append(task1)

        return project
    

if __name__ == '__main__':
    unittest.main()