import unittest
from app import create_app, db
from app.models import Task

class TaskTestCase(unittest.TestCase):
    
    def setUp(self):
        # Task
        self.NAME_PRUEBA = 'Tarea 1'
        self.DESCRIPTION_PRUEBA = 'Make Money'
        self.STARTDATE_PRUEBA = '1/1/0'
        self.DEADLINE_PRUEBA = '8/7/24'
        self.PRIORITY_PRUEBA = 'High'
        self.DIFFICULTY_PRUEBA = 'Hard'
        self.STATE_PRUEBA = 'In Progress'

        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_task(self):
        
        task = self.__get_task()

        # db.session.add(user)
        # db.session.commit()

        self.assertEqual(task.name, self.NAME_PRUEBA)
        self.assertEqual(task.description, self.DESCRIPTION_PRUEBA)
        self.assertEqual(task.start_date, self.STARTDATE_PRUEBA)
        self.assertEqual(task.deadline, self.DEADLINE_PRUEBA)
        self.assertEqual(task.priority, self.PRIORITY_PRUEBA)
        self.assertEqual(task.difficulty, self.DIFFICULTY_PRUEBA)
        self.assertEqual(task.state, self.STATE_PRUEBA)

    def __get_task(self):
        task = Task()
        task.name = self.NAME_PRUEBA
        task.description = self.DESCRIPTION_PRUEBA
        task.start_date = self.STARTDATE_PRUEBA
        task.deadline = self.DEADLINE_PRUEBA
        task.priority = self.PRIORITY_PRUEBA
        task.difficulty = self.DIFFICULTY_PRUEBA
        task.state = self.STATE_PRUEBA

        return task
    

if __name__ == '__main__':
    unittest.main()