from typing import List
from flask_mail import Message
from app import mail

class Email:
    
    def send_email(subject: str, recipients: List[str], body: str) -> None:
        msg = Message(subject, sender = 'gproyectoramandu@gmail.com', recipients = recipients)
        msg.body = body
        mail.send(msg)