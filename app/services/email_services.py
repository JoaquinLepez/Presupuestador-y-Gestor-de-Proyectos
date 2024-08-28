from typing import List
from flask_mail import Message
from app import mail
from .emailserver_service import EmailServer_Service
import os
import email

class EmailService:
    
    def create(subject: str, recipients: List[str], body: str) -> Message:
        msg = Message(subject, recipients = recipients, body = body)
        return msg
    
    def send(msg: Message) -> None:
        mail.send(msg)

    def read(email_address: str, password: str, mailbox: str = 'inbox', search_criteria: str = 'ALL') -> List[str]:
        server = EmailServer_Service()
        server.login(email_address, password)
        server.set_mailbox(mailbox)
        data = server.email_server.search(None, search_criteria)
        emails = []
        
        for num in data[0].split():
            msg_data = server.mail_server.fetch(num, '(RFC822)')
            raw_email = msg_data[0][1]
            msg = emails.message_from_bytes(raw_email)
            
            
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        emails.append(part.get_payload(decode=True).decode())
            else:
                emails.append(msg.get_payload(decode=True).decode())
        
        
        server.mail_server.logout()

        return emails
    
    def read_latest(email_address: str, password: str = os.environ.get('EMAIL_KEY'), mailbox: str = 'inbox') -> str:
        server = EmailServer_Service()
        server.login(email_address, password)
        server.set_mailbox(mailbox)
        
        # Buscar todos los correos
        status, data = server.email_server.search(None, 'ALL')
        
        # Obtener el último correo
        if status == 'OK':
            # Los IDs de los correos están en data[0], y están separados por espacios
            email_ids = data[0].split()
            
            # Obtener el último ID de correo
            latest_email_id = email_ids[-1]
            
            # Fetch (obtener) el contenido del último correo
            status, msg_data = server.email_server.fetch(latest_email_id, '(RFC822)')
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)
            
            # Extraer el contenido del mensaje
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        latest_email = part.get_payload(decode=True).decode()
            else:
                latest_email = msg.get_payload(decode=True).decode()
            
            # Cerrar la conexión con el servidor
            server.email_server.logout()
            
            # Retornar el contenido del último correo
            return latest_email

