import unittest
from app import create_app
from app.services import EmailService
from unittest.mock import patch
from app.services import WerkzeugSecurity

class EmailServiceTestCase(unittest.TestCase):
    def setUp(self):
        # Email params
        self.security = WerkzeugSecurity()
        self.PASSWORD = 'RamanduRamandu2024!'
        self.SUBJECT = 'Test Email: Test Subject'
        self.RECIPIENTS = ['gproyectoramandu@gmail.com']
        self.BODY = self.security.generate_password(password = self.PASSWORD)
        self.SENDER = 'gproyectoramandu@gmail.com'

        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
          
    @patch('app.services.EmailService.send')
    def test_send_email(self, mock_send):
        test_email = EmailService.create(self.SUBJECT, self.RECIPIENTS, self.BODY)
        EmailService.send(test_email)
        self.assertTrue(mock_send.called)
        
        mock_send.assert_called_with(test_email)
        
        self.assertEqual(test_email.subject, self.SUBJECT)
        self.assertEqual(test_email.recipients, self.RECIPIENTS)
        self.assertEqual(test_email.body, self.BODY)

    def test_send_emailservice(self):
        test_email = EmailService.create(self.SUBJECT, self.RECIPIENTS, self.BODY)
        EmailService.send(test_email)

        lastest_email = EmailService.read_latest(self.SENDER)
        self.assertTrue(self.security.check_password(lastest_email.strip(),self.PASSWORD))
        

if __name__ == '__main__':
    unittest.main()
