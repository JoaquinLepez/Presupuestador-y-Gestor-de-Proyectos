import unittest, os
from app import create_app, db
from app.models import Role, Permission

class RoleTestCase(unittest.TestCase):
    
    def setUp(self):
        # Role
        self.NAME_TEST = 'Admin'

        # Permission
        self.PERMISSION_TEST1 = "add_task"
        self.PERMISSION_TEST2 = "delete_task"

        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_role(self):
        
        role = self.__get_role()

        self.assertEqual(role.name, self.NAME_TEST)
        self.assertIsNotNone(role.permissions)
        self.assertEqual(role.permissions[0].name, self.PERMISSION_TEST1)
        self.assertEqual(role.permissions[1].name, self.PERMISSION_TEST2)
         

    def __get_role(self) -> Role:
        role = Role()
        role.name = self.NAME_TEST

        permission1 = Permission()
        permission1.name = self.PERMISSION_TEST1

        permission2 = Permission()
        permission2.name = self.PERMISSION_TEST2

        role.permissions.append(permission1)
        role.permissions.append(permission2)

        return role
    

if __name__ == '__main__':
    unittest.main()