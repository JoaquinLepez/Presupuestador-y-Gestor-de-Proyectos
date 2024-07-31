import unittest, os
from app import create_app, db
from app.models import Permission
from app.services import PermissionService


permission_service = PermissionService()

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

    def test_permission_save(self):
        permission = self.__get_permission()

        permission_service.save(permission)

        self.assertGreaterEqual(permission.id,1)
        self.assertEqual(permission.name, self.NAME_TEST)
    
    def test_permission_delete(self):
        permission = self.__get_permission()
        permission_service.save(permission)

        permission_service.delete(permission)
        self.assertIsNone(permission_service.find(permission.id))
    
    def test_permission_all(self):
        permission = self.__get_permission()
        permission_service.save(permission)

        permissions = permission_service.all()
        self.assertGreaterEqual(len(permissions), 1)

    def test_permission_find(self):
        permission = self.__get_permission()
        permission_service.save(permission)

        permission_find = permission_service.find(1)
        self.assertIsNotNone(permission_find)
        self.assertEqual(permission_find.id, permission.id)

    def __get_permission(self) -> Permission:
        permission = Permission()
        permission.name = self.NAME_TEST

        return permission
    

if __name__ == '__main__':
    unittest.main()


    