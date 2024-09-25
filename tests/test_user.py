import unittest, os
from app import create_app, db
from app.models import User, UserData
from app.services import UserService

user_service = UserService()

class UserTestCase(unittest.TestCase):
    
    def setUp(self):
        # User
        self.USERNAME_TEST = 'ramandu'
        self.PASSWORD_TEST = '123456'
        self.EMAIL_TEST = 'test@test.com'

        self.FIRSTNAME_TEST = 'Juan'
        self.LASTNAME_TEST = 'Salleme'
        self.PHONE_TEST = '542604660415'
        self.ADDRESS_TEST = 'Address 1234'
        self.CITY_TEST = 'San Rafael'
        self.COUNTRY_TEST = 'Argentina'
    
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

        user_service.delete(user.id)
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

        user_data = self._get_user_data()
        user.data = user_data

        return user
    
    def _get_user_data(self) -> UserData:
        
        user_data = UserData()
        user_data.firstname = self.FIRSTNAME_TEST
        user_data.lastname = self.LASTNAME_TEST
        user_data.phone = self.PHONE_TEST
        user_data.address = self.ADDRESS_TEST
        user_data.city = self.CITY_TEST
        user_data.country = self.COUNTRY_TEST

        return user_data

if __name__ == '__main__':
    unittest.main()
