from flask_mail import Message
from flask import current_app
from app import mail 
from flask import render_template

def send_email(subject, recipients, body, sender=None):
    sender = sender or current_app.config['MAIL_USERNAME']
    msg = Message(subject=subject, recipients=recipients, sender=sender)
    msg.body = body
    mail.send(msg)

def send_deal_email(deal, subject, recipients, sender=None):
    message_body = f"📧 Sending to {recipients}:\n  {deal['title']} - {deal['description']}"
    # Replace with actual email logic (SMTP/SendGrid/Mailgun/etc.)
    sender = sender or current_app.config['MAIL_USERNAME']
    msg = Message(subject=subject, recipients=recipients, sender=sender)
    msg.body = message_body
    mail.send(msg)
