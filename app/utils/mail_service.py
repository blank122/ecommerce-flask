from flask_mail import Message
from flask import current_app
from app import mail 

def send_email(subject, recipients, body, sender=None):
    sender = sender or current_app.config['MAIL_USERNAME']
    msg = Message(subject=subject, recipients=recipients, sender=sender)
    msg.body = body
    mail.send(msg)
