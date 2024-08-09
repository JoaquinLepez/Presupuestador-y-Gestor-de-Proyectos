from flask_mail import Message
from app import mail

class Email:
    
    def send_email(subjet, recipients, body):
        msg = Message(subjet, sender = 'gproyectoramandu@gmail.com', recipients = recipients)
        msg.body = body
        mail.send(msg)