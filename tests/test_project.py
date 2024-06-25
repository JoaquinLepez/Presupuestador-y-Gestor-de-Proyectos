import unittest
from app import create_app, db
from app.models import Project, Task
from app.services import ProjectService

project_service = ProjectService()

class ProjectTasteCase(unittest.TestCase):

    def setUp(self):   
        # Project
        self.NAME_PRUEBA = "mi proyecto"
        self.DESCRIPTION_PRUEBA = "esta es la descripcion de mi proyecto"
        self.START_DATE_PRUEBA = "1/1/2024"
        self.DEADLINE_PRUEBA = "28/2/2024"
        self.STATE_PRUEBA = "en proceso"
        # Task 1
        self.TASK1_NAME_PRUEBA = "prueba número 1"
        self.TASK1_DESCRIPTION_PRUEBA = "esta es la descripcion de mi prueba número 1"
        self.TASK1_START_DATE_PRUEBA = "1/1/2024"
        self.TASK1_DEADLINE_PRUEBA = "28/2/2024"
        self.TASK1_PRIORITY_PRUEBA = "alta prioridad"
        self.TASK1_DIFFICULTY_PRUEBA = "elevada"
        self.TASK1_STATE_PRUEBA = "en proceso"

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

        self.assertTrue(project.name, self.NAME_PRUEBA)
        self.assertTrue(project.description, self.DESCRIPTION_PRUEBA)
        self.assertTrue(project.start_date, self.START_DATE_PRUEBA)
        self.assertTrue(project.deadline, self.DEADLINE_PRUEBA)
        self.assertTrue(project.state, self.STATE_PRUEBA)
        self.assertIsNotNone(project.task[0])
        self.assertEqual(project.task[0].name, self.TASK1_NAME_PRUEBA)
    
    def test_project_save(self):
        project = self.__get_project()

        project_service.save(project)

        self.assertGreaterEqual(project.id,1)
        self.assertEqual(project.name, self.NAME_PRUEBA)
        self.assertEqual(project.description, self.DESCRIPTION_PRUEBA)
        self.assertEqual(project.start_date, self.START_DATE_PRUEBA)
        self.assertEqual(project.deadline, self.DEADLINE_PRUEBA)
        self.assertEqual(project.state, self.STATE_PRUEBA)
        self.assertIsNotNone(project.task[0])
        self.assertEqual(project.task[0].name, self.TASK1_NAME_PRUEBA)
    
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

    def __get_project(self):

        task1 = Task()
        task1.name = self.TASK1_NAME_PRUEBA
        task1.description = self.TASK1_DESCRIPTION_PRUEBA
        task1.start_date = self.TASK1_START_DATE_PRUEBA
        task1.deadline = self.TASK1_DEADLINE_PRUEBA
        task1.priority = self.TASK1_PRIORITY_PRUEBA
        task1.difficulty = self.TASK1_DIFFICULTY_PRUEBA
        task1.state = self.TASK1_STATE_PRUEBA

        project = Project()
        project.name = self.NAME_PRUEBA
        project.description = self.DESCRIPTION_PRUEBA
        project.start_date = self.START_DATE_PRUEBA
        project.deadline = self.DEADLINE_PRUEBA
        project.state = self.STATE_PRUEBA

        project.task.append(task1)

        return project
    

if __name__ == '__main__':
    unittest.main()