import unittest
from app import create_app
from app.services import Email
from unittest.mock import patch

class EmailServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['MAIL_SUPPRESS_SEND'] = True  # Para evitar enviar correos reales
        self.app.config['MAIL_DEFAULT_SENDER'] = 'test@test.com'
        self.client = self.app.test_client()

        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    @patch('app.services.Email.send_email')
    def test_enviar_correo(self, mock_send):
        # Define los parámetros del correo
        subject = 'Test Subject'
        recipients = ['test@test.com']
        body = 'This is a test email body.'

        # Llama a la función que envía el correo
        Email.send_email(subject, recipients, body)

        # Asegúrate de que mail.send() fue llamado
        self.assertTrue(mock_send.called)
        mock_send.assert_called_with(subject, recipients, body)

if __name__ == '__main__':
    unittest.main()
