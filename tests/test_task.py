import unittest, os
from app import create_app, db
from app.models import Task
from app.services import TaskService
from datetime import datetime

task_service = TaskService()

class TaskTestCase(unittest.TestCase):
    
    def setUp(self):
        # Task
        self.NAME_TEST = 'Tarea 1'
        self.DESCRIPTION_TEST = 'Make Money'
        self.STARTDATE_TEST = datetime(2024,2,14,14,14,14)
        self.DEADLINE_TEST = datetime(2024,3,14,14,14,14)
        self.PRIORITY_TEST = 'High'
        self.DIFFICULTY_TEST = 'Hard'
        self.STATE_TEST = 'In Progress'

        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_task(self):   
        task = self.__get_task()

        self.assertEqual(task.name, self.NAME_TEST)
        self.assertEqual(task.description, self.DESCRIPTION_TEST)
        self.assertEqual(task.start_date, self.STARTDATE_TEST)
        self.assertEqual(task.deadline, self.DEADLINE_TEST)
        self.assertEqual(task.priority, self.PRIORITY_TEST)
        self.assertEqual(task.difficulty, self.DIFFICULTY_TEST)
        self.assertEqual(task.state, self.STATE_TEST)

    def test_task_save(self):
        task = self.__get_task()

        task_service.save(task)

        self.assertGreaterEqual(task.id,1)
        self.assertEqual(task.name, self.NAME_TEST)
        self.assertEqual(task.description, self.DESCRIPTION_TEST)
        self.assertEqual(task.start_date, self.STARTDATE_TEST)
        self.assertEqual(task.deadline, self.DEADLINE_TEST)
        self.assertEqual(task.priority, self.PRIORITY_TEST)
        self.assertEqual(task.difficulty, self.DIFFICULTY_TEST)
        self.assertEqual(task.state, self.STATE_TEST)

    def test_task_delete(self):
        task = self.__get_task()
        task_service.save(task)

        task_service.delete(task.id)
        self.assertIsNone(task_service.find(task.id))
    
    def test_task_all(self):
        task = self.__get_task()
        task_service.save(task)

        tasks = task_service.all()
        self.assertGreaterEqual(len(tasks), 1)

    def test_task_find(self):
        task = self.__get_task()
        task_service.save(task)

        task_find = task_service.find(1)
        self.assertIsNotNone(task_find)
        self.assertEqual(task_find.id, task.id)
    
    def test_task_find_by_name(self):
        task = self.__get_task()
        task_service.save(task)

        task_find = task_service.find_by_name(task.name)
        self.assertIsNotNone(task_find)
        self.assertEqual(task_find.id, task.id)

    def __get_task(self) -> Task:
        task = Task()
        task.name = self.NAME_TEST
        task.description = self.DESCRIPTION_TEST
        task.start_date = self.STARTDATE_TEST
        task.deadline = self.DEADLINE_TEST
        task.priority = self.PRIORITY_TEST
        task.difficulty = self.DIFFICULTY_TEST
        task.state = self.STATE_TEST

        return task
    

if __name__ == '__main__':
    unittest.main()