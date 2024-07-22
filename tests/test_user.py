import unittest,os
from app import create_app, db
from app.models import User
from app.services import UserService

user_service = UserService()

class UserTestCase(unittest.TestCase):
    
    def setUp(self):
        # User
        self.USERNAME_TEST = 'ramandu'
        self.PASSWORD_TEST = '123456'
        self.EMAIL_TEST = 'test@test.com'
    
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user(self):  
        user = self.__get_user()

        self.assertEqual(user.email, self.EMAIL_TEST)
        self.assertEqual(user.username, self.USERNAME_TEST)
        self.assertEqual(user.password, self.PASSWORD_TEST)

    def test_user_save(self):
        user = self.__get_user()

        user_service.save(user)

        self.assertGreaterEqual(user.id, 1)
        self.assertEqual(user.email, self.EMAIL_TEST)
        self.assertEqual(user.username, self.USERNAME_TEST)
        self.assertIsNotNone(user.password)
        self.assertTrue(user_service.check_auth(user.username, self.PASSWORD_TEST))
    
    def test_user_delete(self):
        user = self.__get_user()
        user_service.save(user)

        user_service.delete(user)
        self.assertIsNone(user_service.find(user.id))

    def test_user_all(self):
        user = self.__get_user()
        user_service.save(user)

        users = user_service.all()
        self.assertGreaterEqual(len(users), 1)
    
    def test_user_find(self):
        user = self.__get_user()
        user_service.save(user)

        user_find = user_service.find(1)
        self.assertIsNotNone(user_find)
        self.assertEqual(user_find.id, user.id)
        self.assertEqual(user_find.email, user.email)

    def __get_user(self) -> User:
        user = User()
        user.username = self.USERNAME_TEST
        user.email = self.EMAIL_TEST
        user.password = self.PASSWORD_TEST

        return user
    

if __name__ == '__main__':
    unittest.main()
