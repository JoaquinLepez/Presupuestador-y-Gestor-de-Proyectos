import unittest,os
from app import create_app, db
from app.models import UserData

class UserDataTestCase(unittest.TestCase):
    
    def setUp(self):
        # User Data
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

    def test_userdata(self):
        
        user_data = self.__get_userdata()
        
        self.assertEqual(user_data.firstname, self.FIRSTNAME_TEST)
        self.assertEqual(user_data.lastname, self.LASTNAME_TEST)
        self.assertEqual(user_data.phone, self.PHONE_TEST)
        self.assertEqual(user_data.address, self.ADDRESS_TEST)
        self.assertEqual(user_data.city, self.CITY_TEST)
        self.assertEqual(user_data.country, self.COUNTRY_TEST)

    def __get_userdata(self) -> UserData:
        
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
