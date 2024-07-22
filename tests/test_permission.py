import unittest, os
from app import create_app, db
from app.models import Permission

class PermissionTestCase(unittest.TestCase):
    
    def setUp(self):
        # Role
        self.NAME_TEST = 'add_task'

        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_permission(self): 
        permission = self.__get_permission()

        self.assertEqual(permission.name, self.NAME_TEST)

    def __get_permission(self) -> Permission:
        permission = Permission()
        permission.name = self.NAME_TEST

        return permission
    

if __name__ == '__main__':
    unittest.main()


    